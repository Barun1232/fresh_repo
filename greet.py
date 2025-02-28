print("Hi, I’m Barun from Nepal!")
print("I’m getting better at Git every day!")
print("I'm just starting and knowing about git.")

#simple calculator 
while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter first number: "))
        operater = input("Enter the operater (+, -, *, /): ")
        if operater == "+":
            result = num1 + num2
            print(f"{num1} {operater} {num2} is ({result})")

        elif operater == "-":
            result = num1 - num2
            print(f"{num1} {operater} {num2} is ({result})")

        elif operater == "*":
            result = num1 * num2
            print(f"{num1} {operater} {num2} is ({result})")

        elif operater == "/":
            result = num1 / num2
            print(f"{num1} {operater} {num2} is ({result})")
        else:
            raise ValueError("Enter operaters (+, -, *, /) ")
        
        while True:
            calc_again = input("Do you want to calculate again (yes/no): ")

            if calc_again == "yes":
                break
            elif calc_again == "no":
                print("Thanks for using!")
                exit()
            else:
                raise ValueError("Enter yes/no")
                
                
    except ValueError as e:
        if str(e) in ["Enter operaters (+, -, *, /) ",
                      "Enter yes/no"]:
                  print(e)
        else:
            print("Please enter a valid number for the temperature!")

        
        
        
        
    
