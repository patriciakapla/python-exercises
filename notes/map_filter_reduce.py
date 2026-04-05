"""
MAP
map data
(similar to what we did with list comprehension)
iterates through an object, can modify the elements in it.

map is an interator, so when you call it, it gets "empty"
if you want to keep using it, transform it into a list
list(map(function, list))

syntax:
map(function, list)


FILTER
Optional filter

REDUCE
reduces an iterable to one value
"""


def print_iter(iterator):
    print(*list(iterator), sep="\n")
    print()


products = [
    {"name": "Product 5", "price": 1.8},
    {"name": "Product 6", "price": 35},
    {"name": "Product 4", "price": 62.6},
    {"name": "Product 3", "price": 12.4},
    {"name": "Product 7", "price": 6.66},
    {"name": "Product 2", "price": 21.1},
]


# WITH LIST COMPREHENSION:
from functools import partial  # function that receives a function


def raise_prices(value, multiplier):
    return round(value * multiplier, 2)


raise15percent = partial(raise_prices, multiplier=1.15)


new_products = [
    {**product, "price": raise15percent(product["price"])} for product in products
]

print_iter(new_products)


def update_prices(product):
    return {**product, "price": raise15percent(product["price"])}


mapped_products = map(update_prices, products)

mapped_products2 = list(
    map(
        lambda product: {**product, "price": round(product["price"] * 1.15, 2)},
        products,
    )
)

num_list = [1, 3, 6, 3, 6, 7]

new_num_list = list(map(lambda num: num * 3, num_list))

print_iter(mapped_products)
print_iter(mapped_products2)

print_iter(new_num_list)


# FILTER

filtered_products = [p for p in products if p["price"] > 10]

# SAME AS:

filtered_products = filter(lambda p: p["price"] > 15, products)

print_iter(filtered_products)


# REDUCE


total = 0
for p in products:
    total += p["price"]

print(total)

# same as:

from functools import reduce


def reduceFunction(acumulator, product):
    return acumulator + product["price"]


total2 = reduce(reduceFunction, products, 0.00)  # reduce(function, item, initial value)

print(total2)
