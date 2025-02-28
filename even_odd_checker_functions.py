def get_integer_input():
    """
    Prompts the user to enter an integer and returns the integer value.
    """
    while True:
        try:
            user_input = int(input("Please enter an integer: "))
            return user_input
        except ValueError:
            print("That's not a valid integer. Please try again.")

def check_even_odd(number):
    """
    Determines if the given number is even or odd.

    Parameters:
    number (int): The integer to check.

    Returns:
    str: A formatted string message indicating whether the number is even or odd.
    """
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

def main():
    """
    Main program flow.
    """
    number = get_integer_input()
    result = check_even_odd(number)
    print(result)

if __name__ == "__main__":
    main()