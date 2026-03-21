from random import randint

def multiply(*args):
    total = 1
    for number in args:
        total *= number
    return total

multiplication = multiply(1,2,3,4,5)
print(multiplication)


def is_even_or_odd(number):
    if number % 2 == 0:
        return f"{number} is even"
    return f"{number} is odd"


print(is_even_or_odd(randint(1, 100)))


