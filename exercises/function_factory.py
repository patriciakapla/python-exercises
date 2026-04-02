"""
Exercise: Function Factory

Create a function that generates new functions by preloading arguments.

Requirements:

Accept a callable and initial arguments
Return a function that accepts additional arguments
Call the original function with all arguments combined

Concepts:
Higher-order functions
Closures
*args
Partial application
"""

import math


def add(*args):
    return sum(args)


def multiply(*args):
    return math.prod(args)


def create_function(executor, *original_args):
    def function(*args):
        return executor(*original_args, *args)

    return function


add_5 = create_function(add, 5)
multiply_10 = create_function(multiply, 10)

print(add_5(5))
print(multiply_10(10, 5))
