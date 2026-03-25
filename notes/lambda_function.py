'''
one line function without a name

lambda parameter: returned_element


'''

# intro to the actual note on lambda function (how to sort a dictionary with lambda)
my_list = [5, 24, 65, 3, 33, 45, 21, 75, 101]
my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)

my_list = [5, 24, 65, 3, 33, 45, 21, 75, 101]

other_list = sorted(my_list) # creates a sorted shallow copy of the list
print(other_list)


# sorting a dictionary with a regular function
people_list = [
    {'first-name': 'Janine', 'last-name': 'McCullen'},
    {'first-name': 'Carla', 'last-name': 'Soares'},
    {'first-name': 'John', 'last-name': 'Keyes'},
    {'first-name': 'Lucas', 'last-name': 'Johnson'},
]

def my_sort(item):
    return item['first-name']     # defines function to return the value for a key. the item will be people list, and the function will be called through the sort method:
people_list.sort(key=my_sort)    # pass the function as the key argument to the sort method, so it knows the sorting should follow the 'name' key. people_list is the argument for the 'item' parameter, in the my_sort function.


# sorting the dictionary with lambda function

people_list_2 = [
    {'first-name': 'Janine', 'last-name': 'McCullen'},
    {'first-name': 'Carla', 'last-name': 'Soares'},
    {'first-name': 'John', 'last-name': 'Keyes'},
    {'first-name': 'Lucas', 'last-name': 'Johnson'},
]

people_list_2.sort(key=lambda item: item['last-name'])
#                        parameter: returns key of dictionary

# sorted(people_list_2, key=lambda item: item['name'])      sorted shallow copy


print('\nsorted by first name with regular function:')
for item in people_list:
    print(item)

print('\nsorted by last name with lambda:')
for item in people_list_2:
    print(item)


# PEP8 recommends creating a function that executes the lambda function, instead of assigning it to a variable

not_recommended = lambda parameter: parameter


# create function to execute lambda
def execute(function, *args):
    return function(*args)
print(
    execute(lambda x, y: x + y, 2, 3) 
)

# example with closure, but overcomplicating it
def create_multiplier(multiplier):
    def multiply(number):
        return number * multiplier
    return multiply

duplicate = create_multiplier(2)
print(duplicate(4))



lamb_duplicate = execute(
    lambda multiplier: lambda number: multiplier * number, 2  # passing the multiplier (2), otherwise execute( wont get its second argument, in this case, the multiplier)
    )
 
print(lamb_duplicate(10))