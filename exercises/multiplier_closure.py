"""
Exercise: Multiplier Closure

Description:
Create a function that takes a multiplier as an argument and returns
a function that multiplies numbers using that value.

Concepts used:
- closure
- higher-order functions
- nested functions
"""

def create_multiplier(multiplier):
    def multiply(number):
        return multiplier * number
    return multiply

multiply_by_2 = create_multiplier(2)
multiply_by_3 = create_multiplier(3)
multiply_by_4 = create_multiplier(4)

print(multiply_by_2(2))
print(multiply_by_3(2))
print(multiply_by_4(2))

