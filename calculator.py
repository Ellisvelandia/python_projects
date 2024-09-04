operator = input("Enter a operator  ( + - * /): ")

num1 = float(input("Eneter the 1st number: "))
num2 = float(input("Eneter the 2st number: "))

if operator == "+":
    result = num1 + num2
    print(round(result))
elif operator == "-":
    result = num1 - num2
    print(round(result))
elif operator == "*":
    result = num1 * num2
    print(round(result))
elif operator == "/":
    result = num1 / num2
    print(round(result))
else:
    print(f"{operator} is not a valid operator")    
