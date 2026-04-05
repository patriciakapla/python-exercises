def zipper(list1, list2):
    maximum_range = min(len(list1), len(list2))
    return [(list1[i], list2[i]) for i in range(maximum_range)]


list1 = ["Porto Alegre", "Florianópolis", "Belo Horizonte"]
list2 = ["RS", "SC", "MG", "SP"]

print(zipper(list1, list2))


# SAME AS:
print(list(zip(list1, list2)))
# zip gets the shorter list length as the maximum range.
# to get the bigger list, do this:

from itertools import zip_longest

print(list(zip_longest(list1, list2, fillvalue="N/A")))


#############################


li1 = [3, 4, 1, 7, 0]
li2 = [5, 1, 5, 8]


added_list = [x + y for x, y in zip(li1, li2)]
print(added_list)


# def add_indexes(li1, li2):
#     max_range = min(len(li1), len(li2))
#     return [li1[i] + li2[i] for i in range(max_range)]


# li3 = add_indexes(li1, li2)
# print(li3)
