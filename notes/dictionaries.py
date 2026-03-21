''' DICTIONARIES '''


example = dict(first_key='first value', second_key='second value',)

# better:
client = {
    'first_name': 'Johanna', 
    'last_name': 'Anderson',
    'birth_year': 1968,
    'active': False,
    'weight': 65.5,
    'billings': [32.5, 88.7, 93.4, 101],
    'addresses': [
        {'label': 'home', 'street_name': '55th avenue', 'street_number': 32,},   
        {'label': 'work', 'street_name': '63th avenue', 'street_number': 123,}
        ]       
    }



# KeyError exception
# print(client['points'])
if client.get('points') is None:      # get() gets a key 
    print("The key 'points' doesn't exist")
else:
    print(f"The value of 'points' is: {client['points']}")
#print(client.get('points')) # can be used instead of client['points'] 
# can pass a default value:  client.get('points', '0')


# setting a new key
client['points'] = 600
print(client['points'])

# removing a key
del client['points']


# dictionary length
print(len(client))



print()
# dictionary keys
print(list(client.keys()))
for key in client:
    print(key)



print()
# dictionary values
print(list(client.values()))
for value in client.values():
    print(value)



print()
# dictionary items
print(list(client.items()))     # each item is a tuple
for key, value in client.items():
    print(key, ':', value)



print()
# setting a default value for a key
client.setdefault('points', 0) 


print()
# copy returns a shallow copy
# new_client = client
# new_client['first_name'] = 'Janine'     # this will also change the key in "client"

# with copy, this is avoided. but it returns a shallow copy - it copies only the immutable data types. 
new_client = client.copy()
new_client['first_name'] = 'Janine'
print(client)
print(new_client)
# the mutable data types inside the dictionary are still directioned to the original variable:
new_client['billings'][1] = 0
print()
print(client['billings'][1])
print(new_client['billings'][1])


# to get a deep copy, import copy
import copy
a = {
    'k1': 'v1',
    'k2': ['v2', 'v3', 'v4'],
}
b = copy.deepcopy(a)
b['k2'][0] = 'new value'
print(a['k2'])
print(b['k2'])


print()
# pop is different than the list: it pops an item with the given key (like del)
billings = new_client.pop('billings')
print(billings)
# print(new_client['billings'])                   #Key Error

print()
# pop item removes last key in dictionary (like list pop)
last_key = new_client.popitem()
print(last_key)
print(new_client)


print()
# update -> updates values, creates new keys
new_client.update({
    'first_name': 'Jessica',
    'other_attribute': 'other value', 
})
new_client.update(last_name='Tuttle', birth_year=1987)

new_keys_tuples = ('new_key_1', 'new value 1'), ('new_key_2', 2)

new_client.update(new_keys_tuples)
print(new_client)