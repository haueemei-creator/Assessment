def second_largest(arr):
    """
    Returns the second largest unique number in the array.
    Returns None if there are fewer than 2 unique values.
    """
    if not arr or len(arr) < 2:
        return None
    
    # Get unique values
    unique_nums = set(arr)
    
    if len(unique_nums) < 2:
        return None
    
    # Sort unique values and get second last
    sorted_unique = sorted(unique_nums)
    return sorted_unique[-2]

def main():
    # Test cases
    test_cases = [
        [3, 1, 4, 1, 5, 9, 7], 
    ]
    
    for i, arr in enumerate(test_cases):
        result = second_largest(arr)
        print(f"Test {i+1}: {arr} -> Second largest: {result}")

if __name__ == "__main__":
    main()