def classify_age_nested(age):
    """
    Classify age using nested if-elif-else conditionals
    Age ranges:
    - 0-12: Child
    - 13-19: Teen
    - 20-59: Adult
    - 60+: Senior
    """
    if age >= 0:
        if age <= 12:
            return "Child"
        elif age <= 19:
            return "Teen"
        elif age <= 59:
            return "Adult"
        else:
            return "Senior"
    else:
        return "Invalid age (negative)"

def classify_age_simple(age):
    """
    Classify age using simple if-elif-else conditionals
    """
    if age < 0:
        return "Invalid age (negative)"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teen"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"

def classify_age_dictionary(age):
    """
    Classify age using dictionary-based approach
    """
    if age < 0:
        return "Invalid age (negative)"
    
    age_ranges = {
        (0, 12): "Child",
        (13, 19): "Teen",
        (20, 59): "Adult",
        (60, float('inf')): "Senior"
    }
    
    for (min_age, max_age), category in age_ranges.items():
        if min_age <= age <= max_age:
            return category
    
    return "Invalid age"

def classify_age_ternary(age):
    """
    Classify age using ternary operators
    """
    if age < 0:
        return "Invalid age (negative)"
    
    return ("Child" if age <= 12 else
            "Teen" if age <= 19 else
            "Adult" if age <= 59 else
            "Senior")

def classify_age_match(age):
    """
    Classify age using match statement (Python 3.10+)
    """
    if age < 0:
        return "Invalid age (negative)"
    
    match age:
        case age if age <= 12:
            return "Child"
        case age if age <= 19:
            return "Teen"
        case age if age <= 59:
            return "Adult"
        case _:
            return "Senior"

# Test the functions with various age values
def test_age_classification():
    """Test all age classification functions with sample ages"""
    test_ages = [-5, 0, 5, 12, 13, 16, 19, 20, 30, 45, 59, 60, 75, 100]
    
    print("Age Classification Results:")
    print("=" * 50)
    
    for age in test_ages:
        print(f"Age: {age:3d} | ", end="")
        print(f"Nested: {classify_age_nested(age):8s} | ", end="")
        print(f"Simple: {classify_age_simple(age):8s} | ", end="")
        print(f"Dict: {classify_age_dictionary(age):8s} | ", end="")
        print(f"Ternary: {classify_age_ternary(age):8s} | ", end="")
        print(f"Match: {classify_age_match(age):8s}")

# Interactive function to get user input
def interactive_age_classifier():
    """Interactive function to classify user's age"""
    print("\nInteractive Age Classifier")
    print("=" * 30)
    
    while True:
        try:
            age_input = input("Enter an age (or 'quit' to exit): ")
            
            if age_input.lower() == 'quit':
                print("Goodbye!")
                break
            
            age = int(age_input)
            category = classify_age_nested(age)
            print(f"Age {age} is classified as: {category}")
            
        except ValueError:
            print("Please enter a valid number or 'quit'")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    # Run the test function
    test_age_classification()
    
    # Run the interactive classifier
    interactive_age_classifier()
