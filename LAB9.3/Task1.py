def sum_even_odd_numbers(numbers):
    """
    Calculate the sum of even and odd numbers in a given list.
    
    This function takes a list of integers and returns a tuple containing
    the sum of all even numbers and the sum of all odd numbers separately.
    
    Args:
        numbers (list): A list of integers to be processed.
        
    Returns:
        tuple: A tuple containing (sum_of_even, sum_of_odd) where:
            - sum_of_even (int): The sum of all even numbers in the list
            - sum_of_odd (int): The sum of all odd numbers in the list
            
    Raises:
        TypeError: If the input is not a list or contains non-integer values.
        
    Example:
        >>> result = sum_even_odd_numbers([1, 2, 3, 4, 5, 6])
        >>> print(result)
        (12, 9)
        >>> even_sum, odd_sum = sum_even_odd_numbers([10, 15, 20, 25])
        >>> print(f"Even sum: {even_sum}, Odd sum: {odd_sum}")
        Even sum: 30, Odd sum: 40
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    sum_even = 0
    sum_odd = 0
    
    for num in numbers:
        if not isinstance(num, int):
            raise TypeError("All elements in the list must be integers")
        
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    
    return sum_even, sum_odd


# AI-Generated Docstring (using AI assistance)
def sum_even_odd_numbers_ai_docstring(numbers):
    """
    Computes the sum of even and odd numbers separately from a list of integers.
    
    Takes a list of integers and returns a tuple with two values: the sum of all
    even numbers and the sum of all odd numbers. Even numbers are those divisible
    by 2, while odd numbers are those that are not.
    
    Parameters:
        numbers (list[int]): The list of integers to process
        
    Returns:
        tuple[int, int]: A tuple containing (even_sum, odd_sum)
        
    Raises:
        TypeError: If input is not a list or contains non-integer elements
        
    Examples:
        >>> sum_even_odd_numbers_ai_docstring([1, 2, 3, 4, 5])
        (6, 9)
        >>> sum_even_odd_numbers_ai_docstring([2, 4, 6, 8])
        (20, 0)
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    sum_even = 0
    sum_odd = 0
    
    for num in numbers:
        if not isinstance(num, int):
            raise TypeError("All elements in the list must be integers")
        
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    
    return sum_even, sum_odd


# Test cases and example usage
if __name__ == "__main__":
    # Test case 1: Mixed even and odd numbers
    test_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result1 = sum_even_odd_numbers(test_list1)
    print(f"Test 1 - List: {test_list1}")
    print(f"Manual docstring function result: {result1}")
    print(f"Even sum: {result1[0]}, Odd sum: {result1[1]}")
    print()
    
    # Test case 2: Only even numbers
    test_list2 = [2, 4, 6, 8, 10]
    result2 = sum_even_odd_numbers(test_list2)
    print(f"Test 2 - List: {test_list2}")
    print(f"Manual docstring function result: {result2}")
    print(f"Even sum: {result2[0]}, Odd sum: {result2[1]}")
    print()
    
    # Test case 3: Only odd numbers
    test_list3 = [1, 3, 5, 7, 9]
    result3 = sum_even_odd_numbers(test_list3)
    print(f"Test 3 - List: {test_list3}")
    print(f"Manual docstring function result: {result3}")
    print(f"Even sum: {result3[0]}, Odd sum: {result3[1]}")
    print()
    
    # Test case 4: Empty list
    test_list4 = []
    result4 = sum_even_odd_numbers(test_list4)
    print(f"Test 4 - List: {test_list4}")
    print(f"Manual docstring function result: {result4}")
    print(f"Even sum: {result4[0]}, Odd sum: {result4[1]}")
    print()
    
    # Test case 5: Negative numbers
    test_list5 = [-3, -2, -1, 0, 1, 2, 3]
    result5 = sum_even_odd_numbers(test_list5)
    print(f"Test 5 - List: {test_list5}")
    print(f"Manual docstring function result: {result5}")
    print(f"Even sum: {result5[0]}, Odd sum: {result5[1]}")
    print()
    
    # Compare both functions with same input
    print("=== COMPARISON: Manual vs AI-Generated Docstring Functions ===")
    comparison_list = [1, 2, 3, 4, 5, 6]
    manual_result = sum_even_odd_numbers(comparison_list)
    ai_result = sum_even_odd_numbers_ai_docstring(comparison_list)
    
    print(f"Input list: {comparison_list}")
    print(f"Manual docstring function: {manual_result}")
    print(f"AI docstring function: {ai_result}")
    print(f"Results match: {manual_result == ai_result}")
    print()
    
    # Error handling test
    print("=== ERROR HANDLING TEST ===")
    try:
        sum_even_odd_numbers("not a list")
    except TypeError as e:
        print(f"TypeError caught: {e}")
    
    try:
        sum_even_odd_numbers([1, 2, "three", 4])
    except TypeError as e:
        print(f"TypeError caught: {e}")


print("\n" + "="*60)
print("DOCSTRING COMPARISON ANALYSIS")
print("="*60)
print("""
MANUAL DOCSTRING (Google Style):
- More detailed and comprehensive
- Includes detailed Args section with type information
- Provides clear Returns section with tuple structure explanation
- Includes Raises section for error handling
- Contains multiple examples with expected outputs
- More verbose and explanatory

AI-GENERATED DOCSTRING:
- More concise and to the point
- Uses modern type hints (list[int], tuple[int, int])
- Clear and direct language
- Includes basic examples
- Less verbose but still informative
- Follows modern Python documentation standards

BOTH DOCSTRINGS:
- Follow proper docstring conventions
- Include parameter descriptions
- Provide return value information
- Include examples
- Handle error cases
- Are well-structured and readable

CONCLUSION:
The manual docstring is more comprehensive and detailed, while the AI-generated
docstring is more concise and uses modern type hints. Both are effective,
but the choice depends on the project's documentation style preferences.
""")
