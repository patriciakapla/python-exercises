"""
LIST COMPREHENISON
List comprehension is a quick way to create lists from iterables.

MAPPING WITH LIST COMPREHENSION
mapping transforms data from list into another one. Lists must be of same length

FILTER DATA
Filter data that goes into the new list when using list comprehension

DICTIONARY AND SET COMPREHENSION

"""

import pprint  # module with pprint() function that formats the print


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


# more verbose way to do it, without comprehension. It allows inserting other logics inside the for, maybe select the numbers that will go into the list, or something else.
my_list = []

for number in range(10):
    my_list.append(number)

print(my_list)


# LIST COMPREHENSION - cut way to the form above
numbers = [number for number in range(10)]
print(numbers)

# what will be inlcuded in the list for each iteration through the iterable is signaled before the for. In this case, is "number".

other_list = [number * 2 for number in range(10)]
print(other_list)


def multiplication_fn(x, y):
    return x * y


def division_fn(x, y):
    return x / y


multiplication = [multiplication_fn(number, 2) for number in numbers]
division = [division_fn(number, 2) for number in numbers]


print()
print("multiplication", multiplication)
print("division", division)
print()
# also allows to include simple logics. In this case the logic included is "number * 2", and this is what will be appended to the list.


# MAP
# grabs the data from a list and transforms it (or not), to include it in another list. both lists must be of same length

products = [
    {"name": "p1", "price": 20},
    {"name": "p2", "price": 10},
    {"name": "p3", "price": 30},
]

new_products = [product for product in products]

print(new_products)
print(*new_products, sep="\n")

# The above example generates a new list with dictionaries same as the original list.
# You can select only one key, but then the result will be only a list with the values of the keys
# print()

# new_products = [
#     product['name'] for product in products
# ]

# print(new_products)
# print(*new_products, sep='\n')
print()


# you can modify the values of a given key unpacking all arguments in the new dictionary.
# supposing the prices of the products raised 5%:
new_products = [{**product, "price": product["price"] * 1.05} for product in products]
print(new_products)
print(*new_products, sep="\n")
print()


# It's possible to map including ternary if conditions:
# If only prices of products with price <= 10 will be raised:
other_products = [
    (
        {**product, "price": product["price"] * 1.05}
        if product["price"] <= 10
        else {**product}
    )
    for product in products
]
print(other_products)
print(*other_products, sep="\n")

print()

# difference between function p(), created in this module with pprint, and print():

print(other_products)
print()
p(other_products)


#  FILTERS
# while mapping comes BEFORE the for, filters come AFTER the for:

other_list_1 = [n for n in range(10) if n < 5]  # if n < is the filter
p(other_list_1)

one_more_product_list = [
    (
        {**product, "price": product["price"] * 1.05}
        if product["price"] <= 10
        else {**product}
    )
    for product in products
    if product["price"] >= 20
]

print()
p(one_more_product_list)


# List comprehension with more than one for
values = []

for x in range(3):
    for y in range(3):
        values.append((x, y))

p(values)
print()

values = [(x, y) for x in range(3) for y in range(3)]

p(values)
print()


# list comprehention within the value of a list comprehention

values = [[letter for letter in "name"] for _ in range(3)]

p(values)
print()


multiplication_and_division = [
    [multiplication_fn(number, 2), division_fn(number, 2)]
    for number in numbers
    # if 2 < number < 12
]
p(multiplication_and_division)


operations = [
    "devil" if number == 6 else [multiplication_fn(number, 2), division_fn(number, 2)]
    for number in numbers
    # if 2 < number < 12
]
p(operations)


my_string = "Desce a lenha, Maricota"
new_string = [my_string[index : index + 2] for index in range(0, len(my_string), 2)]

print(new_string)

new_string = ".".join(
    [my_string[index : index + 2] for index in range(0, len(my_string), 2)]
)

print(new_string)


names = ["Alana", "John", "Lila", "Mario", "Nelson"]
new_names = [name[:-1].lower() + name[-1].upper() for name in names]
print(new_names)


#  FLAT MAP


new_numbers = [[number, number**2] for number in range(11)]

p(new_numbers)

flat = [y for x in new_numbers for y in x]

print(flat)


# DICTIONARY COMPREHENSION
product = {"name": "Blue Pen", "price": 1.2, "category": "Office", "in_stock": 45}

print(product.items())

dc = {
    key: value.upper() if isinstance(value, str) else value
    for key, value in product.items()
    if key != "in_stock"
}
print(dc)


looks_like_dictionary = [("a", "value a"), ("b", "value b"), ("c", "value c")]

mapped_list_to_dict = {key: value for key, value in looks_like_dictionary}

print(mapped_list_to_dict)


this_is_a_set = {f" 2 ** {i} = {2**i} " for i in range(11)}
print(this_is_a_set)
