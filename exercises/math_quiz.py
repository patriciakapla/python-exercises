"""
Exercise: Math Quiz

Description:
Multiple-choice math quiz that accepts answers by option or result.

Concepts used:
- dictionaries
- loops
- input validation
- type conversion
- conditional logic
"""

''' GLOBAL VARIABLES'''
math_problems = [
    {
        'problem': '3+3?',
        'choices': ['3', '6', '4', '8'],
        'correct_option': 2,
        'correct_value': 6,

    },
    {
        'problem': '5*5?',
        'choices': ['25', '55', '10', '51'],
        'correct_option': 1,
        'correct_value': 25,

    },
    {
        'problem': '40/2?',
        'choices': ['5', '10', '15', '20'],
        'correct_option': 4,
        'correct_value': 20,

    },
]

def validate_input(user_input):
    try:
        user_input = int(user_input)
        return user_input
    except ValueError:
        print("Invalid input")

right_answers = 0

''' MAIN PROGRAM '''
print('*********', 
      'MATH QUIZ', 
      '*********', sep="\n", end="\n\n")

for question in math_problems:
    print('Problem: ', question['problem'])
    for index, value in enumerate(question['choices']):
        print("[", index + 1, "] ", value, sep="")
    while True:
        answer = input("Enter your choice or the result: ")
        valid_input = validate_input(answer)
        if valid_input or valid_input == 0:
            break
    if valid_input == question['correct_option'] or valid_input == question['correct_value']:
        print("Right answer! :)", end="\n\n")
        right_answers += 1
    else:
        print("Wrong answer :(", end="\n\n")

print(f"Score: {right_answers}/{len(math_problems)}")


