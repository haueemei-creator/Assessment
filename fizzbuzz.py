def fizzbuzz():
    """Print numbers 1 to 100 with FizzBuzz rules."""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def main():
    fizzbuzz()

if __name__ == "__main__":
    main()