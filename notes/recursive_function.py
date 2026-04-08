"""
RECURSIVE FUNCTIONS / RECURSION
Function that return itself / function that call itself
Used to break problems into smaller parts
Every recursive function must have:
-   A problem to be solved. It must be divisible in smaller problems, and it must be uniform
-   A recursive case that solve this smaller problem
-   A base case that stops recursion (conditional statement)
Example:
factorial -> 5! = 5 * 4 * 3 * 2 * 1 = 120

"""


def recursive_overflow(start=0, end=10):
    # Recursive case: count until it gets to the end
    start += 1
    return recursive_overflow(start, end)


# STACK OVERFLOW
# when call stack is full! security limit. The above function returns RecursionError: maaximum recursion depth exceeded. This is STACK OVERFLOW, when you exceed the number of recursions python supports (1000).
# A BASE CASE (CONDITIONAL STATEMENT) must be given to stack overflow be avoided!:


def recursive(start=0, end=10):
    if start >= end:  # base case
        return end
    print(start, end)
    start += 1
    return recursive(start, end)


print(recursive())


# Since the recursion limit in python's stack is 1000, even if the function is correctly defined, with a base case, it can still return an error, since there might be more functions on the stack. Example: if recursive(0, 1000) is called, and you have other functions on the stack, it wont get to 1000 recursions.
# This can be worked around using from sys import setrecursionlimit.


# In python it's not usual to use recursive functions, usually a simple loop does the case. But, depending on the problem, recursion might be more performative (rarely)


# FACTORIAL is a common example of recursive functions
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print()
print("factorial")
print(factorial(3))
