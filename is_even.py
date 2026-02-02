def is_even(n):
    return n%2==0

def main():
    try:
        n=int(input("Enter an Integer: "))
        result=is_even(n)
        print(f"{n} is {'even' if result else 'odd'}")
    except ValueError:
        print("Please enter a valid integer.")
        
if __name__=="__main__":
    main()