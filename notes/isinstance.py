"""
isinstance() is used to find if an object is of a given type

syntax: isinstance(object, type)
returns item and a boolean
"""

a_list = ["a", 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {"name": "Karl"}]

# this list is not ideal, since its items is of diferent typs.
# Heterogenic lists demand if conditions to test its type, what breaks the SOLID's Liskov Substitution Principle.
# if all data in my list are of the same type, i dont have to worry with testing mixed types when using it.

# for item in a_list:
#   item.add(6)         to do this, you must check type first, since not all data types suport add
#   print(item, isinstance(item, set))
for item in a_list:
    if isinstance(item, set):
        item.add(6)
        print(item, isinstance(item, set))
    if isinstance(item, str):
        item = item.upper()
        print(item, isinstance(item, str))
    if isinstance(item, (int, float)):
        print(item, item * 2)
    else:
        print("outro", type(item))
        print()
