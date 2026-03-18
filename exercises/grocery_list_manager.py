"""
Grocery List Manager

Description:
Create a simple command-line program that allows the user to manage a
grocery list. The user can add items, remove items by their index, view
all items in the list, or exit the program. The program continuously
prompts the user for actions and validates input to ensure only valid
options and numbers are accepted.

Concepts used:

- while loops
- functions
- lists
- enumerate
- conditional statements
- try/except (error handling)
- user input validation

"""

import os

def validate_input(message, allowed_values):
    user_input = input(message).lower()
    while user_input not in allowed_values:
        print("Invalid input")
        user_input = input(message).lower()
    return user_input

def validate_int(message):
    while True: 
        try:
            item = int(input(message))
            break
        except ValueError:
            print("Invalid input")
    return item

''' MAIN PROGRAM ''' 
grocery_list = []
while True:
    print("*" * 12)
    print("GROCERY LIST")
    print("*" * 12)
    user_input = validate_input("What would you like to do? " \
              "[a]dd | [r]emove | [l]ist | [e]xit: ", "arle")
    if user_input == "e":
        break
    elif user_input == "a":
        item = input("What would you like to add? ")
        grocery_list.append(item)
        os.system("clear")
    elif user_input == "r":
        item_index = validate_int("What item would you like to remove [index]? ")
        try:
            grocery_list.pop(item_index)
            os.system("clear")
        except IndexError:
            print("Invalid index")
            continue
    elif user_input == "l":
        for index, item in enumerate(grocery_list):
            print(index, item)


