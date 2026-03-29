"""
TRY, EXCEPT, ELSE AND FINALLY
errors can't be silenced, they must be avoided and treated


RAISE
used to force an exception (manually trigger it)

"""

try:
    ...
except:
    ...

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter a number: "))
#     c = a / b
#     print(f"{a} / {b} = {c}")
#     print("This is a string"[200])
#     print(b[300])
#     print(d)
# except ZeroDivisionError:
#     print("A number can't be divided by zero.")
# except ValueError:
#     print("Enter a valid number")
# except NameError:  # gets print(d)
#     print("Name not defined")
# except Exception as error:  # creates a variable for the error
#     print("Unknown error")  # gets all not treated errors
#     print("msg", error)
#     print("name", error.__class__.__name__)

a = 1
b = 0
try:
    print(f"Trying to divide {a} by {b}...")
    print(a / b)
except ZeroDivisionError:
    print("Can't divide by 0")
else:
    print("Will execute if there's no error")
finally:
    print("Always executes")


#  RAISE
# used to force an exception (manually trigger it)


def division(n, d):
    treat_division_by_zero(d)
    treat_type(n, d)
    return n / d


def treat_division_by_zero(d):
    if d == 0:
        raise ZeroDivisionError("Division by 0 is impossible")
    return True


def treat_type(n, d):
    if not isinstance(n, (int, float)) or not isinstance(d, (int, float)):
        raise TypeError("Arguments must be numbers")
    return True


print(division(9, 2))
