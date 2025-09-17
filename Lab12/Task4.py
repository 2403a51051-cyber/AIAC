import argparse
import random
import string
import time
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


@dataclass
class Stock:
    symbol: str
    open_price: float
    close_price: float

    @property
    def pct_change(self) -> float:
        if self.open_price == 0:
            return 0.0
        return (self.close_price - self.open_price) / self.open_price * 100.0


def random_symbol(length: int = 4) -> str:
    letters = string.ascii_uppercase
    return "".join(random.choice(letters) for _ in range(length))


def simulate_stocks(n: int, seed: Optional[int] = 42) -> List[Stock]:
    if seed is not None:
        random.seed(seed)
    stocks: List[Stock] = []
    for _ in range(n):
        symbol = random_symbol(random.randint(3, 5))
        open_price = round(random.uniform(5.0, 500.0), 2)
        # Simulate close: +/- up to 15%
        change_factor = 1.0 + random.uniform(-0.15, 0.15)
        close_price = round(open_price * change_factor, 2)
        stocks.append(Stock(symbol, open_price, close_price))
    return stocks


def heapify(arr: List[Stock], n: int, i: int, key=lambda s: s.pct_change) -> None:
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and key(arr[left]) > key(arr[largest]):
        largest = left
    if right < n and key(arr[right]) > key(arr[largest]):
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, key)


def heap_sort(stocks: List[Stock], key=lambda s: s.pct_change, reverse: bool = True) -> List[Stock]:
    # For reverse=True we build a max-heap and then reverse at the end
    arr = stocks[:]  # work on a copy
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0, key)
    if reverse:
        arr.reverse()
    return arr


def build_hash_map(stocks: List[Stock]) -> Dict[str, Stock]:
    return {s.symbol: s for s in stocks}


def search_symbol(hash_map: Dict[str, Stock], symbol: str) -> Optional[Stock]:
    return hash_map.get(symbol)


def benchmark_sorting(stocks: List[Stock]) -> Tuple[float, float]:
    start = time.perf_counter()
    _ = heap_sort(stocks, key=lambda s: s.pct_change, reverse=True)
    heap_time = time.perf_counter() - start

    start = time.perf_counter()
    _ = sorted(stocks, key=lambda s: s.pct_change, reverse=True)
    std_time = time.perf_counter() - start

    return heap_time, std_time


def benchmark_search(hash_map: Dict[str, Stock], symbols: List[str]) -> float:
    start = time.perf_counter()
    for sym in symbols:
        _ = hash_map.get(sym)
    return time.perf_counter() - start


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Task 4: Real-Time Stock Data Sorting & Searching")
    parser.add_argument("--n", type=int, default=50000, help="Number of stocks to simulate")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--show_top", type=int, default=10, help="Print top N movers")
    parser.add_argument("--lookup", type=str, default=None, help="Symbol to lookup (optional)")
    return parser.parse_args()


def main() -> None:
    args = cli()
    stocks = simulate_stocks(args.n, seed=args.seed)

    # Sorting comparisons
    heap_time, std_time = benchmark_sorting(stocks)
    sorted_heap = heap_sort(stocks, key=lambda s: s.pct_change, reverse=True)
    sorted_std = sorted(stocks, key=lambda s: s.pct_change, reverse=True)

    # Validate that ranking orders are identical for fairness
    identical_order = [s.symbol for s in sorted_heap] == [s.symbol for s in sorted_std]

    print(f"Stocks simulated: {len(stocks)}")
    print(f"Heap Sort time: {heap_time:.6f}s | sorted() time: {std_time:.6f}s | Same order: {identical_order}")

    print(f"\nTop {args.show_top} by % change (Heap Sort):")
    for s in sorted_heap[: args.show_top]:
        print(f"{s.symbol:>5}  open={s.open_price:8.2f}  close={s.close_price:8.2f}  %chg={s.pct_change:7.2f}")

    # Build hash map for instant lookup
    hmap = build_hash_map(stocks)

    # If user provided a symbol, look it up
    if args.lookup:
        res = search_symbol(hmap, args.lookup.upper())
        if res is None:
            print(f"\nLookup: {args.lookup} not found")
        else:
            print(
                f"\nLookup: {res.symbol}  open={res.open_price:.2f}  close={res.close_price:.2f}  %chg={res.pct_change:.2f}"
            )

    # Benchmark hash map lookups vs dict directly (same structure under the hood)
    # Use a mix of existing and random symbols
    sample_symbols = [stocks[i].symbol for i in range(0, len(stocks), max(1, len(stocks) // 1000))]
    sample_symbols += [random_symbol() for _ in range(500)]

    t_hashmap = benchmark_search(hmap, sample_symbols)

    print(f"\nLookup batch size: {len(sample_symbols)} | Hash map lookup time: {t_hashmap:.6f}s")
    print("Note: Python dict is a hash map; custom wrapper mainly demonstrates usage and API design.")


if __name__ == "__main__":
    main()


