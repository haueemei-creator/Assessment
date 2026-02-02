def larger(x, y):
    return (x + y + abs(x - y)) // 2

def main():
    try:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        result = larger(x, y)
        print(f"The larger value is: {result}")
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()