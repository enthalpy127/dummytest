try:
    # Get number input from the user
    num = int(input("Enter a number to check: "))

    # If the remainder when divided by 2 is 0, it's even
    if num % 2 == 0:
        print(f"{num} is an Even number.")
    else:
        print(f"{num} is an Odd number.")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
