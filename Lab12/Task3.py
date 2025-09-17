import argparse
import csv
import math
import os
import random
from dataclasses import dataclass
from typing import Callable, Iterable, List, Optional, Sequence, Tuple

import matplotlib.pyplot as plt


Point = Tuple[float, float]
Route = List[int]


def set_reproducible_seed(seed: Optional[int]) -> None:
    if seed is None:
        return
    random.seed(seed)


def load_points_from_csv(csv_path: str) -> List[Point]:
    points: List[Point] = []
    with open(csv_path, "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            if len(row) == 1 and "," in row[0]:
                parts = row[0].split(",")
                x, y = float(parts[0].strip()), float(parts[1].strip())
            else:
                x, y = float(row[0]), float(row[1])
            points.append((x, y))
    return points


def generate_random_points(num_points: int, spread: float = 100.0) -> List[Point]:
    return [(random.random() * spread, random.random() * spread) for _ in range(num_points)]


def euclidean_distance(a: Point, b: Point) -> float:
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return math.hypot(dx, dy)


def route_length(points: Sequence[Point], route: Route, return_to_start: bool = True) -> float:
    if len(route) <= 1:
        return 0.0
    total = 0.0
    for i in range(len(route) - 1):
        total += euclidean_distance(points[route[i]], points[route[i + 1]])
    if return_to_start:
        total += euclidean_distance(points[route[-1]], points[route[0]])
    return total


def greedy_tsp(points: Sequence[Point], start_index: int = 0) -> Route:
    n = len(points)
    if n == 0:
        return []
    if start_index < 0 or start_index >= n:
        start_index = 0
    unvisited = set(range(n))
    route: Route = [start_index]
    unvisited.remove(start_index)
    current = start_index
    while unvisited:
        next_idx = min(unvisited, key=lambda j: euclidean_distance(points[current], points[j]))
        route.append(next_idx)
        unvisited.remove(next_idx)
        current = next_idx
    return route


def two_opt_swap(route: Route, i: int, k: int) -> Route:
    return route[:i] + list(reversed(route[i:k + 1])) + route[k + 1:]


def simulated_annealing(
    points: Sequence[Point],
    initial_route: Route,
    return_to_start: bool = True,
    initial_temperature: float = 100.0,
    final_temperature: float = 1e-3,
    cooling_rate: float = 0.995,
    max_iterations: int = 100000,
) -> Route:
    if not initial_route:
        return []
    current_route = initial_route[:]
    best_route = current_route[:]
    current_cost = route_length(points, current_route, return_to_start)
    best_cost = current_cost

    temperature = initial_temperature
    n = len(current_route)
    iteration = 0
    while temperature > final_temperature and iteration < max_iterations:
        i = random.randint(0, n - 2)
        k = random.randint(i + 1, n - 1)
        candidate_route = two_opt_swap(current_route, i, k)
        candidate_cost = route_length(points, candidate_route, return_to_start)
        delta = candidate_cost - current_cost

        if delta < 0 or random.random() < math.exp(-delta / temperature):
            current_route = candidate_route
            current_cost = candidate_cost
            if current_cost < best_cost:
                best_route = current_route
                best_cost = current_cost

        temperature *= cooling_rate
        iteration += 1

    return best_route


def make_random_route(n: int) -> Route:
    r = list(range(n))
    random.shuffle(r)
    return r


def plot_routes(
    points: Sequence[Point],
    routes: List[Tuple[str, Route, str]],
    return_to_start: bool = True,
    title: str = "AUV Swarm Route Optimization",
    save_path: Optional[str] = None,
) -> None:
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    plt.figure(figsize=(9, 7))
    plt.scatter(xs, ys, c="#333333", s=30, zorder=5, label="Sensors")

    for name, route, color in routes:
        if not route:
            continue
        path_x = [points[i][0] for i in route]
        path_y = [points[i][1] for i in route]
        if return_to_start and len(route) > 1:
            path_x.append(points[route[0]][0])
            path_y.append(points[route[0]][1])
        plt.plot(path_x, path_y, label=name, linewidth=2.0, color=color, alpha=0.9)

    for idx, (x, y) in enumerate(points):
        plt.text(x, y, str(idx), fontsize=8, ha="right", va="bottom")

    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True, linestyle=":", alpha=0.5)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150)
    else:
        plt.show()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Task 3: Route Optimization for AUV Swarm")
    parser.add_argument("--csv", type=str, default=None, help="Path to CSV with x,y per line")
    parser.add_argument("--n", type=int, default=25, help="Number of sensors if generating synthetic data")
    parser.add_argument("--spread", type=float, default=100.0, help="Range of coordinate generation [0, spread]")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--no_return", action="store_true", help="Do not return to start (open tour)")
    parser.add_argument("--start", type=int, default=0, help="Start index for greedy")
    parser.add_argument("--save", type=str, default=None, help="Save plot to path instead of showing")
    parser.add_argument("--sa", action="store_true", help="Use Simulated Annealing to improve greedy route")
    parser.add_argument("--sa_iters", type=int, default=30000, help="Max SA iterations")
    parser.add_argument("--sa_T0", type=float, default=100.0, help="SA initial temperature")
    parser.add_argument("--sa_Tf", type=float, default=1e-3, help="SA final temperature")
    parser.add_argument("--sa_cool", type=float, default=0.995, help="SA cooling rate per step")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    set_reproducible_seed(args.seed)

    if args.csv is not None and os.path.exists(args.csv):
        points = load_points_from_csv(args.csv)
    else:
        points = generate_random_points(args.n, spread=args.spread)

    n = len(points)
    if n == 0:
        print("No points provided.")
        return

    return_to_start = not args.no_return

    random_route = make_random_route(n)
    greedy_route = greedy_tsp(points, start_index=min(max(0, args.start), n - 1))

    optimized_route = greedy_route
    if args.sa:
        optimized_route = simulated_annealing(
            points,
            initial_route=greedy_route,
            return_to_start=return_to_start,
            initial_temperature=args.sa_T0,
            final_temperature=args.sa_Tf,
            cooling_rate=args.sa_cool,
            max_iterations=args.sa_iters,
        )

    random_dist = route_length(points, random_route, return_to_start)
    greedy_dist = route_length(points, greedy_route, return_to_start)
    optimized_dist = route_length(points, optimized_route, return_to_start)

    print("Sensors:", n)
    print(f"Random route length:   {random_dist:.3f}")
    print(f"Greedy route length:   {greedy_dist:.3f}")
    if args.sa:
        print(f"Optimized (SA) length: {optimized_dist:.3f}")
    else:
        print("Optimized route equals greedy (SA disabled)")

    routes_to_plot: List[Tuple[str, Route, str]] = [
        (f"Random ({random_dist:.1f})", random_route, "#8888cc"),
        (f"Greedy ({greedy_dist:.1f})", greedy_route, "#2ca02c"),
    ]
    if args.sa:
        routes_to_plot.append((f"SA ({optimized_dist:.1f})", optimized_route, "#d62728"))

    plot_routes(
        points,
        routes=routes_to_plot,
        return_to_start=return_to_start,
        title="AUV Swarm Route Optimization",
        save_path=args.save,
    )


if __name__ == "__main__":
    main()


