"""
ITERABLES AND ITERATORS
Iterable - has values
Iterator - delivers values from an iterable, one by one. doesn't know other values than the one that is being delivered and the next value


GENERATORS
special type of iterator that produces a sequence of values on demand, one at a time, without storing the entire sequence in memory
Every generator is an iterator, not every iterator is a generator

GENERATOR EXPRESSION
way to create a generator object using the syntax of a list comprehension, only with (), not with []:
generator = (x for x in y)

GENERATOR FUNCTIONS
functions that know how to PAUSE instead of stopping. a regular function returns and stops. a generator pauses until next item is called.
"""

import sys

iterable = ["I", "have", "__iter__"]
# iterator = iterable.__iter__()      SAME AS:
iterator = iter(iterable)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))

#  behind the scenes, "for" calls for next from iterator, until there's no next value, and treats the StopIteration error that is returned if there is no next value to iterate.


# GENERATOR are functions that can stop at a given time.
# Every generator is also an iterator. not all iterators are generators
a_list = [n for n in range(100)]
generator = (
    n for n in range(100)
)  # similar to a tuple, but it isn't tuple comprehension! tuple comprehension doesn't exist.
print(generator)
print(a_list)
# this can be a problem if the range is too long. by using list comprehension the values are already being saved in the memory, what can result in memory and speed problems

print(sys.getsizeof(a_list))
print(sys.getsizeof(generator))
# sys.getsizeof() returns the size of an object, in bytes. the generator is much lighter. Why:
# Generators don't save directly all the data as the list comprehension does. To save the next value, you have to call for next() in generator:

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

print(sys.getsizeof(generator))

for n in generator:
    print(n)

# generators dont have index, length. it isnt saved in the memory. it's only an element to iterate


# GENERATOR FUNCTION
# a regular function ends with RETURN, which stops the function
# a generator pauses each iteration, until next iteration is called.
# for this to be done in a regular function, use yield
# every function with yield is a generator function.
# the "return" in the generator function works like a "raise stop iteration" - raises a StopIteration exception:


def gen(n=0):
    yield 1  # pauses
    print("continue...")
    yield 2
    print("continue...")
    yield 3
    print("stopping...")
    return "stopped"


gen_var = gen(n=0)

print(next(gen_var))
print(next(gen_var))
print(next(gen_var))
# print(next(gen_var))     #  raises StopIteration exception


for (  # executes all the iterators (yield) in the function. doesnt raise StopIteration exception
    n
) in gen_var:
    print(n)


def gen1(n=0, max=10):
    while True:
        yield n
        n += 1
        if n > max:
            return


gen_var1 = gen1()
for n in gen_var1:
    print(n)


# YIELD FROM   -> it's possible to continue a generator through other generator:
def gen2():
    print("gen2")
    yield 1
    yield 2
    yield 3
    print("end of gen2")


def gen3(gen=None):
    print("gen3")
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    print("end of gen3")


def gen4():
    print("gen4")
    yield 10
    yield 20
    yield 30
    print("end of gen4")


gen_var2 = gen3(gen2())
gen_var3 = gen3(gen4())
gen_var4 = gen3()

print()
for n in gen_var2:
    print(n)
print()

for n in gen_var3:
    print(n)
print()

for n in gen_var4:
    print(n)
