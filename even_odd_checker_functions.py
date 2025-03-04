def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is an Even number.")
    else:
        print(f"{number} is an Odd number.")

while True:
    try:
        user_input = int(input("Enter an integer: "))
        check_even_odd(user_input)
    except ValueError:
        print("Please enter a valid integer.")
        continue