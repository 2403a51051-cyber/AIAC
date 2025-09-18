import re

# Pre-compile regex patterns for better performance
MENTION_PATTERN = re.compile(r'@(\w+)', re.IGNORECASE)
HASHTAG_PATTERN = re.compile(r'#([\w-]+)', re.IGNORECASE)

def extract_hashtags_and_mentions(text):
    """
    Extract hashtags and mentions from text using optimized regex.
    
    Args:
        text (str): Input text containing hashtags and mentions
        
    Returns:
        tuple: (mentions_list, hashtags_list) both in lowercase
    """
    if not text:
        return [], []
    
    # Find all matches using pre-compiled patterns
    mentions = [match.lower() for match in MENTION_PATTERN.findall(text)]
    hashtags = [match.lower() for match in HASHTAG_PATTERN.findall(text)]
    
    return mentions, hashtags

def test_extraction():
    """Optimized test cases for hashtag and mention extraction."""
    
    # Streamlined test cases with essential edge cases
    test_cases = [
        ("Hello @alice check #AI and #Python with @Bob", ['alice', 'bob'], ['ai', 'python'], "Basic mixed case"),
        ("@user1, @user2! #tag1. #tag2?", ['user1', 'user2'], ['tag1', 'tag2'], "Punctuation handling"),
        ("@ALICE @Bob #AI #python", ['alice', 'bob'], ['ai', 'python'], "Case conversion"),
        ("", [], [], "Empty input"),
        ("No tags here", [], [], "No tags"),
        ("@user1@user2 #tag1#tag2", ['user1', 'user2'], ['tag1', 'tag2'], "Adjacent tags"),
        ("@user_name123 #crop-2024", ['user_name123'], ['crop-2024'], "Special characters"),
    ]
    
    print("Running optimized tests...\n")
    all_passed = True
    
    for i, (input_text, exp_mentions, exp_hashtags, description) in enumerate(test_cases, 1):
        actual_mentions, actual_hashtags = extract_hashtags_and_mentions(input_text)
        
        mentions_match = actual_mentions == exp_mentions
        hashtags_match = actual_hashtags == exp_hashtags
        passed = mentions_match and hashtags_match
        
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"Test {i}: {status} - {description}")
        
        if not passed:
            print(f"  Input: '{input_text}'")
            print(f"  Expected: mentions={exp_mentions}, hashtags={exp_hashtags}")
            print(f"  Actual:   mentions={actual_mentions}, hashtags={actual_hashtags}")
            all_passed = False
        print()
    
    print("=" * 50)
    print("🎉 ALL TESTS PASSED!" if all_passed else "❌ SOME TESTS FAILED!")
    print("=" * 50)
    
    return all_passed

if __name__ == "__main__":
    # Get input from user
    text = input("Enter text with hashtags and mentions: ")
    
    # Extract mentions and hashtags
    mentions, hashtags = extract_hashtags_and_mentions(text)
    
    # Display results
    print(f"mentions={mentions}, hashtags={hashtags}")
    
    # Uncomment to run tests: test_extraction()
