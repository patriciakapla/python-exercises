"""
ITERTOOLS

COUNT
infinite iterator
import itertools

COMBINATIONS

PERMUTATIONS

PRODUCT - cartesian product


GROUPBY

"""

# COUNT
# infinite iterator
# import itertools
from itertools import count

c1 = count(8, 8)  # begins at 8, step 8
r1 = range(8, 100, 8)  # begins at 8, stops at 100, step 8

print("c1", hasattr(c1, "__iter__"))  # is an iterable
print("c1", hasattr(c1, "__next__"))  # is an iterator

for i in c1:
    print(i)
    if i > 100:
        break


print()
print("range")
for i in r1:
    print(i)
# different from range, count doesnt have an end. if you dont tell it to break, the for will be an infinite loop


# COMBINATIONS
# if you have a list, you can combine indexes
# the order doesnt matter -> it wont match two indexes that were already combined.
from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep="\n")


colors = [
    "blue",
    "yellow",
    "pink",
    "purple",
    "black",
    "white",
    "orange",
    "violet",
    "brown",
    "green",
]

print_iter(combinations(colors, 2))


# PERMUTATIONS
# same as combinations, but it will combine again, even if the items were already matched
print()
print_iter(permutations(colors, 2))


# PRODUCT - cartesian product

tshirts = [
    ["black", "white", "red"],
    ["xs", "s", "m", "l", "xl"],
    ["male", "female"],
    ["cotton", "polyester"],
]

print()
print("CARTESIAN PRODUCT")
print_iter(product(*tshirts))


# GROUPBY
# Group items from a list of dictionaries by a key
from itertools import groupby

students = [
    {"name": "Javier", "grade": "A"},
    {"name": "Kira", "grade": "B"},
    {"name": "Penelope", "grade": "A"},
    {"name": "Samantha", "grade": "C"},
    {"name": "Orlando", "grade": "C"},
    {"name": "Ignacio", "grade": "B"},
]

grades = [
    "A",
    "A",
    "A",
    "A",
    "B",
    "C",
    "A",
]

groups = groupby(grades)

#  for group in groups:
#     print(group)
# this returns a tuple, so you can use key, value in the for:

for key, group in groups:
    print(key)
    print(list(group))

# for it to work, list MUST BE SORTED! otherwise it will generate a repeated group.
print()

groups = groupby(sorted(grades))
for key, group in groups:
    print(key)
    print(list(group))


def order(student):
    return student["grade"]


students_sorted = sorted(students, key=order)


students_groups = groupby(
    students_sorted, key=lambda x: x["grade"]
)  # same as the order() function

for key, group in students_groups:
    print(key)
    for student in group:
        print(student)
