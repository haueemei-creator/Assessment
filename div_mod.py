def int_division_and_remainder(x, y):
    """
    Compute integer division and remainder without using /, %, or built-ins.
    Returns (quotient, remainder) matching Python's behavior:
    - quotient = x // y
    - remainder = x % y
    """
    if y == 0:
        raise ZeroDivisionError("integer division or modulo by zero")
    
    # Handle special cases
    if y == 1:
        return x, 0
    if y == -1:
        return -x, 0
    
    # Determine signs
    is_x_negative = x < 0
    is_y_negative = y < 0
    is_quotient_negative = is_x_negative != is_y_negative
    
    # Work with absolute values
    abs_x = -x if is_x_negative else x
    abs_y = -y if is_y_negative else y
    
    # Perform division by repeated subtraction
    quotient = 0
    remainder = abs_x
    
    while remainder >= abs_y:
        remainder -= abs_y
        quotient += 1
    
    # Apply signs according to Python's rules
    if is_quotient_negative:
        quotient = -quotient
        # Python's remainder has same sign as divisor for negative division
        if remainder != 0:
            quotient -= 1
            remainder = abs_y - remainder
    
    # For positive division, remainder keeps sign of dividend
    elif is_x_negative and remainder != 0:
        remainder = -remainder
    
    return quotient, remainder

if __name__ == "__main__":
    # Interactive version
    print("\n" + "=" * 50)
    print("Interactive mode:")
    try:
        x = int(input("Enter x: "))
        y = int(input("Enter y: "))
        quotient, remainder = int_division_and_remainder(x, y)
        print(f"{x} // {y} = {quotient}")
        print(f"{x} % {y} = {remainder}")
        print(f"Verification: {quotient} * {y} + {remainder} = {quotient * y + remainder}")
    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")