# WAP to get two numbers and operators from the user to perform arithmetic operations. and if uder provide operator then arithmetic then restirct user. using function
def calculator(a, op, b):

    if op == '+':
        print("Addition =", a + b)
    elif op == '-':
        print("Subtraction =", a - b)
    elif op == '*':
        print("Multiplication =", a * b)
    elif op == '/':
        if b != 0:
            print("Division =", a / b)
        else:
            print("Division by zero not allowed")
    else:
        print("Invalid operator")

a = int(input("Enter first number: "))
op = input("Enter operator (+,-,*,/): ")
b = int(input("Enter second number: "))

calculator(a, op, b)