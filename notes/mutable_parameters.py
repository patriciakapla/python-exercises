"""
MUTABLE PARAMETERS AS DEFAULT PARAMETER
"""


def add_client(name, li=[]):
    li.append(name)
    return li


client1 = add_client("Louis")
add_client("Johana", client1)

print(client1)
# THIS IS A PROBLEM!

# when you dont give an argument to the mutable parameter:
# everytime you call the function without giving an argument to the mutable parameter (li), the mutable parameter that will use the same object! So if you try to use the function with another variable, it will be appended to the list created before:

client2 = add_client("Paul")
add_client("Cyrus", client2)

print(client2)
#  you might expect client2 to be ["Paul", "Cyrus"], but it will actually be ['Louis', 'Johana', 'Paul', 'Cyrus']

# to solve this problem and have a new list every time, is to NEVER USE MUTABLE DEFAULT PARAMETERS.

#  BEST PRACTICE:


def best_add_client(name, li=None):
    if li is None:
        li = []
    li.append(name)
    return li


# None doesnt accept append, you have to initialize the list before appending
# best practice because every time you call the function, the list is initialized again, because the whole code of the function is executed, where in the first function the empty list was a parameter and its initialization wasnt executed again.

best_client1 = best_add_client("Louis")
best_add_client("Johana", best_client1)

print(best_client1)

best_client2 = best_add_client("Paul")
best_add_client("Cyrus", best_client2)

print(best_client2)
