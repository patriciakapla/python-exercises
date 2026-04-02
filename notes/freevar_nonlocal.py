"""
Free variables
    not defined in the scope in focus

locals() - function that returns the local namespace - variables that can be accessed in the scope where locals() was called
globals() - function that returns global namespace - global variables

"""


# in this case, inside the inner() func, a is a freevar, since it's not defined inside inner()'s scope.
def outter(x):
    a = x

    def inner():
        print(
            "inner local vars:", *locals(), sep="\n"
        )  # a is local because inner() has access to it.
        print(
            "freevars: ", inner.__code__.co_freevars
        )  # inner is a freevar because it is not defined inside itself. it can be called in its own scope, it will be a case of recursion

        return a

    return inner


inner1 = outter(0)
inner2 = outter(20)

print(inner1())
# print(inner2())
print()
print(*locals(), sep="\n")


# using nonlocal variables (Freevars:)


# def concatenate1(initial_string):
#     final_string = initial_string

#     def final(second_string):
#         final_string += second_string  # UnboundLocalError: cannot access local variable 'final_string' where it is not associated with a value
#         return final_string

#     return final


def concatenate1(initial_string):
    final_string = initial_string

    def final(second_string):
        nonlocal final_string  # use nonlocal to modify nonlocal.
        final_string += second_string
        return final_string

    return final


# concatenate1() REMEMBERS THE VALUE OF A VARIABLE!!!

# NOT THE SAME AS THE FOLLOWING:


def concatenate(initial_string):
    def final(second_string):
        return initial_string + second_string

    return final


good_morning = concatenate("Good Morning, ")
good_morning1 = concatenate1("Good Morning, ")

print(good_morning("John"))
print(good_morning1("John, "))
print(good_morning1("Erick, "))
print(good_morning1("Ginna"))
