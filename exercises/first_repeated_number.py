"""
Exercise: First Repeated Number

Description:
Given a list of integers, return the first number that appears more than once. If no repetition exists, return -1.

"""

integer_lists_list = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]



def get_first_repeated_number(integer_list):
        new_list = []
        for number in integer_list:
            if number not in new_list:
                new_list.append(number)
            else:
                return number
        return -1

for index, integer_list in enumerate(integer_lists_list):
    repeated_number = get_first_repeated_number(integer_list)
    if repeated_number == -1:
         print('No repeated numbers.')
    else:
        print(f"The repeated number in list number {index} is: {repeated_number}")







