while True:
    try:
        # Get number input from the user
        num = int(input("Enter a number to check: "))

        # If the remainder when divided by 2 is 0, it's even
        if num % 2 == 0:
            print(f"{num} is an Even number.")
        else:
            print(f"{num} is an Odd number.")

        # Check if the number is positive, negative, or zero
        if num > 0:
            print(f"{num} is a Positive number.")
        elif num < 0:
            print(f"{num} is a Negative number.")
        else:
            print(f"{num} is Zero.")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")

    continue_input = input("Do you want to check another number? (yes/no): ").strip().lower()
    if continue_input == 'no':
        break
