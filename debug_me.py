# Mini-Project: CLI Calculator 
while True:
    try:
        first_num = int(input("Enter the first number: "))
        second_num = int(input("Enter the second number: "))
        operation = input("Input the operation (+, -, *, /): ")

        if operation == "+":
            result = first_num + second_num
            print(f"Result: {result}")

        elif operation == "-":
            result = first_num - second_num
            print(f"Result: {result}")

        elif operation == "*":
            result = first_num * second_num
            print(f"Result: {result}")

        elif operation == "/":
            result = first_num / second_num
            print(f"Result: {result}")
        
        else:
            raise ValueError("Enter a operation")
        
        while True:
            calculate_again = input("Do you want to calculate again (yes/no): ")
            if calculate_again == "yes":
                break
            elif calculate_again == "no":
                print("Thank you for using! Visit Again.")
                exit()
            else:
                raise ValueError("Enter yes/no")
    except ValueError as e:
        if str(e) in ["Enter a operation",
                      "Enter yes/no"]:
            print(e)
        else:
            print("Please enter a valid number!")
            
    except ZeroDivisionError:
        print("You can't divided by zero")
        continue
