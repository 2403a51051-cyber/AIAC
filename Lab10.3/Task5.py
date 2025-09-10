def div(a, b):
    """Safely divide a by b, handling division by zero."""
    return a / b if b != 0 else "Error: Division by zero."

if __name__ == "__main__":
    try:
        a = float(input("Enter numerator: "))
        b = float(input("Enter denominator: "))
        result = div(a, b)
        print(f"Result: {result}")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")