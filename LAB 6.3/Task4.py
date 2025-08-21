def sum_to_n_for_loop(n):
    """
    Calculate sum of first n numbers using for loop
    """
    if n < 0:
        return "Invalid input: n must be non-negative"
    
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_to_n_while_loop(n):
    """
    Calculate sum of first n numbers using while loop
    """
    if n < 0:
        return "Invalid input: n must be non-negative"
    
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

def sum_to_n_recursion(n):
    """
    Calculate sum of first n numbers using recursion
    """
    if n < 0:
        return "Invalid input: n must be non-negative"
    elif n == 0:
        return 0
    else:
        return n + sum_to_n_recursion(n - 1)

def sum_to_n_list_comprehension(n):
    """
    Calculate sum of first n numbers using list comprehension
    """
    if n < 0:
        return "Invalid input: n must be non-negative"
    
    return sum([i for i in range(1, n + 1)])

def sum_to_n_generator(n):
    """
    Calculate sum of first n numbers using generator expression
    """
    if n < 0:
        return "Invalid input: n must be non-negative"
    
    return sum(i for i in range(1, n + 1))

def sum_to_n_formula(n):
    """
    Calculate sum of first n numbers using mathematical formula: n*(n+1)/2
    """
    if n < 0:
        return "Invalid input: n must be non-negative"
    
    return n * (n + 1) // 2

def sum_to_n_reduce(n):
    """
    Calculate sum of first n numbers using reduce function
    """
    if n < 0:
        return "Invalid input: n must be non-negative"
    
    from functools import reduce
    return reduce(lambda x, y: x + y, range(1, n + 1))

def sum_to_n_accumulate(n):
    """
    Calculate sum of first n numbers using itertools.accumulate
    """
    if n < 0:
        return "Invalid input: n must be non-negative"
    
    from itertools import accumulate
    return list(accumulate(range(1, n + 1)))[-1]

def sum_to_n_controlled_break(n):
    """
    Calculate sum of first n numbers using controlled break
    """
    if n < 0:
        return "Invalid input: n must be non-negative"
    
    total = 0
    for i in range(1, n + 1):
        total += i
        if i == n:  # Controlled break when reaching n
            break
    return total

def sum_to_n_continue_skip(n, skip_multiples_of=None):
    """
    Calculate sum of first n numbers using continue to skip certain numbers
    """
    if n < 0:
        return "Invalid input: n must be non-negative"
    
    total = 0
    for i in range(1, n + 1):
        if skip_multiples_of and i % skip_multiples_of == 0:
            continue  # Skip multiples of specified number
        total += i
    return total

def sum_to_n_nested_loops(n):
    """
    Calculate sum using nested loops (demonstrating loop control)
    """
    if n < 0:
        return "Invalid input: n must be non-negative"
    
    total = 0
    for i in range(1, n + 1):
        for j in range(i):  # Nested loop
            if j == 0:  # Only add once per outer loop iteration
                total += i
                break  # Break inner loop after first iteration
    return total

def sum_to_n_with_validation(n):
    """
    Calculate sum with comprehensive input validation and controlled looping
    """
    # Input validation
    if not isinstance(n, int):
        return "Invalid input: n must be an integer"
    if n < 0:
        return "Invalid input: n must be non-negative"
    if n > 1000000:  # Prevent excessive computation
        return "Invalid input: n is too large (max: 1,000,000)"
    
    # Controlled looping with early exit
    total = 0
    for i in range(1, n + 1):
        total += i
        
        # Safety check to prevent overflow (for very large numbers)
        if total > 10**18:
            return "Result too large to compute safely"
    
    return total

# Test all functions
def test_sum_functions():
    """Test all sum functions with various values"""
    test_values = [0, 1, 5, 10, 100, -5]
    
    print("Sum of First N Numbers - Function Comparison")
    print("=" * 60)
    print(f"{'n':>4} | {'For':>8} | {'While':>8} | {'Recursion':>10} | {'Formula':>8} | {'Generator':>10}")
    print("-" * 60)
    
    for n in test_values:
        if n >= 0:
            for_result = sum_to_n_for_loop(n)
            while_result = sum_to_n_while_loop(n)
            recursion_result = sum_to_n_recursion(n)
            formula_result = sum_to_n_formula(n)
            generator_result = sum_to_n_generator(n)
            
            print(f"{n:>4} | {for_result:>8} | {while_result:>8} | {recursion_result:>10} | {formula_result:>8} | {generator_result:>10}")
        else:
            print(f"{n:>4} | {'Invalid':>8} | {'Invalid':>8} | {'Invalid':>10} | {'Invalid':>8} | {'Invalid':>10}")

def demonstrate_controlled_looping():
    """Demonstrate various controlled looping techniques"""
    print("\nControlled Looping Demonstrations")
    print("=" * 40)
    
    n = 10
    print(f"Sum of first {n} numbers:")
    print(f"Basic for loop: {sum_to_n_for_loop(n)}")
    print(f"While loop: {sum_to_n_while_loop(n)}")
    print(f"Recursion: {sum_to_n_recursion(n)}")
    print(f"Mathematical formula: {sum_to_n_formula(n)}")
    print(f"Generator expression: {sum_to_n_generator(n)}")
    print(f"List comprehension: {sum_to_n_list_comprehension(n)}")
    print(f"Reduce function: {sum_to_n_reduce(n)}")
    print(f"Itertools accumulate: {sum_to_n_accumulate(n)}")
    
    print(f"\nSum of first {n} numbers (skipping multiples of 2): {sum_to_n_continue_skip(n, 2)}")
    print(f"Sum of first {n} numbers (skipping multiples of 3): {sum_to_n_continue_skip(n, 3)}")
    print(f"Nested loops approach: {sum_to_n_nested_loops(n)}")
    print(f"With validation: {sum_to_n_with_validation(n)}")

def interactive_sum_calculator():
    """Interactive function to calculate sum of first n numbers"""
    print("\nInteractive Sum Calculator")
    print("=" * 30)
    
    while True:
        try:
            user_input = input("Enter a number n to calculate sum of first n numbers (or 'quit' to exit): ")
            
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
            
            n = int(user_input)
            
            if n < 0:
                print("Please enter a non-negative number.")
                continue
            
            if n > 1000:
                print(f"Calculating sum of first {n} numbers... (this may take a moment)")
            
            # Use multiple methods to show consistency
            result1 = sum_to_n_for_loop(n)
            result2 = sum_to_n_formula(n)
            
            print(f"Sum of first {n} numbers:")
            print(f"  Using for loop: {result1}")
            print(f"  Using formula: {result2}")
            
            if result1 == result2:
                print("✓ Results match!")
            else:
                print("✗ Results don't match - there's an error!")
                
        except ValueError:
            print("Please enter a valid number or 'quit'")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except RecursionError:
            print(f"Recursion limit reached for n={n}. Try a smaller number.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Run the test function
    test_sum_functions()
    
    # Demonstrate controlled looping
    demonstrate_controlled_looping()
    
    # Run the interactive calculator
    interactive_sum_calculator()
