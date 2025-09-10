def discount(price, category):
    if category == "student":
        return price * 0.9 if price > 1000 else price * 0.95
    else:
        return price * 0.85 if price > 2000 else price

if __name__ == "__main__":
    price = float(input("Enter the price: "))
    category = input("Enter the category (student/other): ").strip().lower()
    final_price = discount(price, category)
    print(f"Discounted price:{final_price:.2f}")