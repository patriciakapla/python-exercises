"""
DECORATORS and DECORATOR FUNCTIONS
to decorate = add, remove, restrict, modify functions
decorator functions are functions that decorate other functions
decorators in python are "syntax sugar" -
decorators are used to make python use the decorator functions in other functions.
with decorators you can add functionalities to a function without modifying its original code, therefore not breaking the Single Responsibility Principle of SOLID.
http://youtube.com/watch?v=3tyaO-OE0K0
"""


def create_function(func):
    def nested(*args, **kwargs):
        for arg in args:
            is_string(arg)
        return func(*args, **kwargs)

    return nested


@create_function  # this is synthax for calling a decorator function
def reverse_string(string):
    print(f"{reverse_string.__name__}")
    return string[::-1]


def is_string(parameter):
    if not isinstance(parameter, str):
        raise TypeError("Parameter must be a string")


# without the use of decorators, the following lines are needed to execute the create_function function:
# check_reverse_string_parameter = create_function(reverse_string)
# reversed_string = check_reverse_string_parameter("Dorohedoro")
# print(reversed_string)


# calling the decorator sends the decorated function as an argument to the decorator function, which returns a new callable that replaces the original function.
# As an example, decorating a function that calls for its __name__, the printed name will be the returned function in the decorator:

reversed_string = reverse_string("Dorohedoro")
print(reversed_string)


# DECORATORS WITH PARAMETERS:


def decorator(func):
    print("decorator 1")

    def inner(*args, **kwargs):
        print("inner")
        result = func(*args, **kwargs)
        return result

    return inner


@decorator
def add(x, y):
    return x + y


ten_plus_five = add(10, 5)
print(ten_plus_five)


# DECORATORS ORDER
# you can decorate a function with innumerable decorators. the order of appliance is the following:


def deco_order(name):
    def deco(func):
        print("Decorator: ", name)

        def innerfunc(*args, **kwargs):
            result = func(*args, **kwargs)
            final = f"{result}, {name}"
            return final

        return innerfunc

    return deco


@deco_order(name="fourth")
@deco_order(name="third")
@deco_order(name="second")
@deco_order(name="first")
def multiply(x, y):
    return x * y


print(multiply(2, 5))
