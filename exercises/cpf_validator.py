"""
Exercise: CPF Validation

Description:
Given a Brazilian CPF (individual taxpayer ID) as a string,
validate its check digits and determine whether it is valid.

Concepts used:
- input validation
- iterative aggregation 
- string manipulation 
- type conversion 
- functions
- conditional logic
"""


def get_valid_cpf_input():
    while True:
        cpf = input("Enter your CPF (numbers only): ")
        sequencial_number = cpf[0] * 11
        if len(cpf) == 11 and cpf.isdigit():
            if cpf != sequencial_number:
                return cpf
            else:
                print("CPF cannot be a repeated sequence")
        else:
            print("Please enter 11 numbers.")

def calculate_weighted_sum(digits, multiplier_value):
    multiplication_sum = 0
    for digit in digits:
        digit = int(digit)
        multiplication_sum += digit * multiplier_value
        multiplier_value -= 1  
    return multiplication_sum

def get_digit(multiplication_sum):
    calculated_digit = (multiplication_sum * 10) % 11
    final_digit = 0 if calculated_digit > 9 else calculated_digit
    return final_digit

def validate_digit(calculated_digit, actual_digit):
    cpf_digit = int(actual_digit)
    if calculated_digit == cpf_digit:
        return True
    return False
    
''' MAIN PROGRAM '''
print("CPF VALIDATION")
cpf = get_valid_cpf_input()

# 10th digit validation (***.***.***-x*)
first_9_digits = cpf[:9]
multiplication_sum_9 = calculate_weighted_sum(first_9_digits, 10)
final_digit_10 = get_digit(multiplication_sum_9)
digit_10_is_valid = validate_digit(final_digit_10, cpf[-2])


# 11th digit validation (***.***.***-*x)
first_10_digits = cpf[:10]    
multiplication_sum_10 = calculate_weighted_sum(first_10_digits, 11) 
final_digit_11 = get_digit(multiplication_sum_10)
digit_11_is_valid = validate_digit(final_digit_11, cpf[-1])

# cpf validation
cpf_is_valid = digit_10_is_valid and digit_11_is_valid
print("Valid CPF" if cpf_is_valid else "Invalid CPF")




