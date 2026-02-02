def reverse_string(s):
    """Reverse a string without using built-in reversal methods."""
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str

def main():
    s = input("Enter a string: ")
    reversed_s = reverse_string(s)
    print(f"Original: {s}")
    print(f"Reversed: {reversed_s}")

if __name__ == "__main__":
    main()