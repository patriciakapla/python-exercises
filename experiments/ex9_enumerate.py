''' GETTING INDEXES OF AN ITERABLE '''


# COUNTER
print("COUNTER")
names = ["Joanna", "Carlos", "Jennifer", "Jonathan", "Helena", "David", "Ellen"]
counter = 0
for name in names:
    print(counter, name)
    counter +=1


print()
# RANGE
print("RANGE")
names = ["Joanna", "Carlos", "Jennifer", "Jonathan", "Helena", "David", "Ellen"]
indexes = range(len(names))
for index in indexes:
    print(index, names[index])


print()
# ENUMERATE FUNCTION-> enumarates each item of an iterable. Generates a new iterable inside the object (each item is a tuple: (index, value).
print("ENUMERATE FUNCTION")
names = ["Joanna", "Carlos", "Jennifer", "Jonathan", "Helena", "David", "Ellen"]
for item in enumerate(names):
    print(item)


# unpacking enumerated lists:
print("UNPACKING ENUMERATED LISTS:")
for index, value in enumerate(names):    # item: tuple (index, value)
    print("Index: ", index, "Value: ", value)

print()

for item in enumerate(names): 
    index, value = item
    print("Index: ", index, "Value: ", value)


print(enumerate(names)) # doesn't work: to print without using for -> convert the object:
print(list(enumerate(names)))