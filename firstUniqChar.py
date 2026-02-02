def first_non_repeating_char(s):
    """
    Find first character that appears exactly once in the string.
    Returns None if no such character exists.
    """
    if not s:
        return None
    
    # Count occurrences
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    
    # Find first character with count == 1
    for char in s:
        if count[char] == 1:
            return char
    
    return None

def main():
    # Test cases
    test_cases = [
        ("parallel", 'p')
    ]
    
    print("Testing first non-repeating character:")
    print("=" * 50)
    
    all_passed = True
    for test_str, expected in test_cases:
        result = first_non_repeating_char(test_str)
        if result != expected:
            all_passed = False
        print(f"'{test_str}' -> '{result}' (expected: '{expected}')")
    
    print("=" * 50)
    if all_passed:
        print("Test passed!")
    else:
        print("Test failed!")

if __name__ == "__main__":
    main()