def print_first_10_multiples_for_loop(n):
    """
    Print first 10 multiples of a number using for loop.
    
    Args:
        n (int): The number to find multiples of
    """
    print(f"First 10 multiples of {n} using FOR loop:")
    print("-" * 40)
    
    for i in range(1, 11):
        multiple = n * i
        print(f"{n} × {i} = {multiple}")
    
    print("-" * 40)


def print_first_10_multiples_while_loop(n):
    """
    Print first 10 multiples of a number using while loop.
    
    Args:
        n (int): The number to find multiples of
    """
    print(f"First 10 multiples of {n} using WHILE loop:")
    print("-" * 40)
    
    i = 1
    while i <= 10:
        multiple = n * i
        print(f"{n} × {i} = {multiple}")
        i += 1
    
    print("-" * 40)


# Main program
if __name__ == "__main__":
    print("MULTIPLES GENERATOR PROGRAM")
    print("=" * 50)
    
    # Test with different numbers
    test_numbers = [5, 7, 12]
    
    for num in test_numbers:
        print()
        print_first_10_multiples_for_loop(num)
        print()
        print_first_10_multiples_while_loop(num)
        print("=" * 50)
    
    # Interactive input
    print("\nEnter a number to see its first 10 multiples:")
    try:
        user_input = int(input("Enter a number: "))
        print()
        print_first_10_multiples_for_loop(user_input)
        print()
        print_first_10_multiples_while_loop(user_input)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
