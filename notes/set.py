'''
SET
mutable data that only accepts immutable data (hashable objects)
curly braces {} - like dicts.
iterable
unordered
efficient to remove duplicated values out of iterables
'''

s1 = {1, 2, 3}


# to create an empty set use set(), otherwise x = {} will create an empty dictionary
s2 = set()




# if the set() constructor is used to create a set with a string as an item, it will treat each character of the string as an item and will iterate through them:
s2 = set('Janine')

print(s2)
# for the set to not treat each character of the string as an item to iterate, declare set with curly braces:
s2={'Janine'}
print(s2)

# sets are efficient in removing duplicated values out of iterables:
l1 = [1, 2, 3, 2, 3, 4, 1, 1, 3, 5]
s1 = set(l1)
l2 = list(s1)

print('list1 - repeated numbers: ', l1)
print('set eliminates repeated items: ', s1)
print('new list w/o repeated numbers: ', l2)

# sets don't accept mutable values:
# s1 = {1, 2, 3, [1, 4, 5]} -> returns TypeError

# they accept tuples, since tuple is a immutable data type.
s1 = {1, 2, 3, (1, 4, 5,)}
print(s1)


#  sets don't have indexes, they don't have an order
# to find values in sets. for loops or:
print(5 in s1)
print(5 not in s1)


''' USEFUL METHODES '''

s1 = set()
s1.add('Janine')      
s1.add(3)
# s1.add(3, 1)     not posible, accepts one value at a time
print(s1)

s1.update('Janine') # .update() ADDS AN ITERABLE! 
print(s1)

# in .update() string must be in a tuple to be considered a single item. 
# can add multiple items at once
s1.update(('Janine', 2, 5))
print(s1)

# s1.clear() -> clears set

# to remove a value, use .discard() passing the value itself:
s1.discard('Janine')
print(s1)


''' USEFUL OPERATORS '''
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2        # unifies sets

print(s3)

s3 = s1 & s3        # intersection between two sets: returns common items
print(s3)


s3 = s1 - s2        # difference: returns the items in the set to the left that aren't in the set to the right
print(s3)           # returns {1}
s3 = s2 - s1
print(s3)           # returns {4}


s3 = s1 ^ s2        # symmetric difference: returns the items that are different in both sets
print(s3)           # returns {1, 4}






