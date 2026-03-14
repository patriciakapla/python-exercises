"""
Simple Calculator

Description:
Command-line calculator that performs basic arithmetic operations
between two numbers. The program repeatedly asks the user for input
until the user chooses to exit.

Features:
- Supports addition, subtraction, multiplication, and division
- Handles invalid numeric input using exception handling
- Runs in a loop until the user exits

Concepts used:
- while loops
- conditional statements
- user input
- exception handling (try/except)
- basic arithmetic operators
"""

print(14*'-')
print('| Calculator |')
print(14*'-')


while True:
    number1_float = None
    number2_float = None

    number1 = input('Enter the first number ([E] to exit): ').lower()
    if number1 == "e":
        print("Exiting...")
        break
    else:
        try:
            number1_float = float(number1)
        except:
            print("Invalid input")
            continue

    number2 = input('Enter the second number: ')

    try:
        number2_float = float(number2)
    except:
        print("Not a valid number")
        continue

    allowed_operators = "*/-+"
    operator = input('Enter an operator (* / + -): ')
    if operator in allowed_operators:
        if operator == "*":
            result = number1_float * number2_float 
        elif operator == "/":
            result = number1_float / number2_float 
        elif operator == "+":
            result = number1_float + number2_float 
        elif operator == "-":
            result = number1_float - number2_float 
        print(f"{number1_float} {operator} {number2_float} = ", result)
    else:
        print("Not a valid operator")
        continue
