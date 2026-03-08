# Simple calculator using while and conditional statements
while True:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    op = input("Enter operator (+, -, *, /): ")

    if op == "+":
        print("Result =", num1 + num2)

    elif op == "-":
        print("Result =", num1 - num2)

    elif op == "*":
        print("Result =", num1 * num2)

    elif op == "/":
        print("Result =", num1 / num2)

    else:
        print("Invalid operator")

    choice = input("Do you want to continue? (yes/no): ")

    if choice == "no":
        break