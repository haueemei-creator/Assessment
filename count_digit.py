def count_threes(n):
    """Count how many times the digit 3 appears in a positive integer."""
    count = 0
    while n > 0:
        if n % 10 == 3:
            count += 1
        n //= 10
    return count

def main():
    try:
        n = int(input("Enter a positive integer: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
        result = count_threes(n)
        print(f"The digit 3 appears {result} time(s) in {n}")
    except ValueError:
        print("Please enter a valid positive integer.")

if __name__ == "__main__":
    main()