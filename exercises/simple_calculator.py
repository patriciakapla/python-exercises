

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
