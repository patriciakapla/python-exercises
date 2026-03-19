
def get_valid_cpf_input():
    while True:
        cpf = input("Enter your CPF (numbers only): ")
        if len(cpf) == 11 and cpf.isdigit:
            break
        else:
            print("Please enter 11 numbers.")
    return cpf

def calculate_weighted_sum(digits):
    multiplier = 10
    multiplication_sum = 0
    for digit in digits:
        digit = int(digit)
        multiplication_sum += digit * multiplier
        multiplier -= 1  
    return multiplication_sum

def validate_digit(prompted_digit, cpf_last_2):
    cpf_digit = int(cpf_last_2)
    if prompted_digit == cpf_digit:
        return True
    else:
        return False
    

''' MAIN PROGRAM '''
print("CPF VALIDATION")

cpf = get_valid_cpf_input()

first_9_digits = cpf[:9]
last_2_digits = cpf[-2:]

multiplication_sum_9 = calculate_weighted_sum(first_9_digits)

calculated_digit_10 = (multiplication_sum_9 * 10) % 11

final_digit_10 = calculated_digit_10 if calculated_digit_10 <= 9 else 0

digit_10_is_valid = validate_digit(final_digit_10, last_2_digits[-2])

print(digit_10_is_valid)

