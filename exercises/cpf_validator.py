
def get_valid_input():
    while True:
        cpf = str(input("Enter your CPF (numbers only): "))
        if len(cpf) == 11 and cpf.isalnum:
            break
        else:
            print("Please enter 11 numbers.")
            continue
    return cpf

def digits_multiplication_sum(first_digits):
    counter = 10
    multiplication_sum = 0
    for digit in first_digits:
        digit = int(digit)
        multiplication_sum += digit * counter
        counter -= 1  
    return multiplication_sum

def validate_digit(prompted_digit, cpf_last_2, index):
    cpf_digit = int(cpf_last_2[index])
    if prompted_digit == cpf_digit:
        return True
    else:
        return False
    

''' MAIN PROGRAM '''
print("CPF VALIDATION")

cpf = get_valid_input()

# first_10_digits = cpf[:10]
# print("first10 ", first_10_digits)
first_9_digits = cpf[:9]
last_2_digits = cpf[-2:]

multiplication_sum_9 = digits_multiplication_sum(first_9_digits)
# multiplication_sum_10 = digits_multiplication_sum(first_10_digits)
# print("mult sum 10 ", multiplication_sum_10)


# prompted_digit_11 = (multiplication_sum_10 * 10) % 11
# print("prompted11 ", prompted_digit_11)


prompted_digit_10 = (multiplication_sum_9 * 10) % 11

digit_10 = prompted_digit_10 if prompted_digit_10 <= 9 else 0
# digit_11 = prompted_digit_11 if prompted_digit_11 <= 9 else 0
# print("digit 11 ", digit_11)


digit_10_is_valid = validate_digit(digit_10, last_2_digits, -2)
# digit_11_is_valid = validate_digit(digit_11, last_2_digits, -1)


print(digit_10_is_valid)
# print(digit_11_is_valid)

