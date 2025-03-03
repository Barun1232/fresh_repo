# Running total calculator
current_total = 0  # Start with zero

while True:
    try:
        # Get initial numbers and operation
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")

        if operation == "+":
            current_total = first_number + second_number
            print(f"Total: {current_total}")
        elif operation == "-":
            current_total = first_number - second_number
            print(f"Total: {current_total}")
        elif operation == "*":
            current_total = first_number * second_number
            print(f"Total: {current_total}")
        elif operation == "/":
            current_total = first_number / second_number
            print(f"Total: {current_total}")
        else:
            print("Enter a valid operation!")
            continue

        # Continue with total
        while True:
            try:
                again = input(f"Continue with {current_total} (yes), start new (new), or stop (no)?: ")
                if again == "new":
                    current_total = 0  # Reset total
                    break
                elif again == "yes":
                    next_number = int(input("Enter a number: "))
                    operation = input("Enter operation (+, -, *, /): ")
                    if operation == "+":
                        current_total = current_total + next_number
                    elif operation == "-":
                        current_total = current_total - next_number
                    elif operation == "*":
                        current_total = current_total * next_number
                    elif operation == "/":
                        current_total = current_total / next_number
                    else:
                        print("Enter a valid operation!")
                        continue
                    print(f"Total: {current_total}")
                elif again == "no":
                    print("Thanks for using!")
                    exit()
                else:
                    raise ValueError("Enter yes, new, or no")
            except ValueError:
                print("Please enter a valid number or option!")
            except ZeroDivisionError:
                print("You can’t divide by zero!")
    except ValueError:
        print("Please enter a valid number!")
    except ZeroDivisionError:
        print("You can’t divide by zero!")