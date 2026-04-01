"""
Exercise: Product List Transformation with Deep Copy

Description:
Given a list of products (dictionaries with name and price), perform the following operations:

1. Increase all product prices by 10%.
2. Sort the products by name in descending order.
3. Sort the products by price in ascending order.

All operations must be performed on deep copies to ensure the original
list remains unchanged.

Concepts used:
- deep copy (copy.deepcopy)
- list of dictionaries manipulation
- lambda functions
- sorting
"""

import copy

products = [
    {"name": "Product 6", "price": 11.2},
    {"name": "Product 3", "price": 78.4},
    {"name": "Product 1", "price": 5.8},
    {"name": "Product 2", "price": 33.65},
    {"name": "Product 4", "price": 15},
    {"name": "Product 5", "price": 21.30},
    {"name": "Product 7", "price": 7.80},
]


def raise_prices(product_list, key, multiplier):
    deep_copy = copy.deepcopy(product_list)
    for item in deep_copy:
        item[key] *= multiplier
        item[key] = round(item[key], 2)
    return deep_copy


products_10percent_raise = raise_prices(products, "price", 1.1)

products_name_sorted = copy.deepcopy(products)
products_name_sorted.sort(key=lambda item: item["name"], reverse=True)


products_price_sorted = copy.deepcopy(products)
products_price_sorted.sort(key=lambda item: item["price"])

print(*products, sep="\n")
print()
print(*products_10percent_raise, sep="\n")
print()
print(*products_name_sorted, sep="\n")
print()
print(*products_price_sorted, sep="\n")
