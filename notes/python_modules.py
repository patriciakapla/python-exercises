"""
MODULES

"""

# IMPORTING ENTIRE MODULE
# doesn't affect performance
# ups: gives access to the module's namespace
# downs: verbose

import sys  # importing sys module

# to use any function from the module, when imported completly, must use the namespace of the module, calling it before the function
# modulename.function()
platform = "My platform"
print(sys.platform)
print(platform)


# IMPORTING A PART OF THE MODULE:
# from moduleName import object1, object2
# ups: not verbose
# downs: can't access module's namespace - watch out for variable names! if the program has a variable name of the same name of the object imported, you won't be able to use it. Example: if from sys import platform, then the platform variable is created (as in the example above), the variable "platform" will subscribe the sys object "platform"

from math import pow, pi

print("This is the module's pi: ", pi)

pi = "This isn't the module's pi"
a = pow(2, 2)
print(pi)
print(a, pow(3, 3))


# if the variable simply CAN'T have a different name, you can import things with a given name:

import random as random_number

random = "This is not the random module"

print(random)
print("This number is from the random module: ", random_number.random())


# bad practice:
from random import *

my_choice = choice(["blue", "yellow", "green", "red"])
print(my_choice)
# imports the whole module as objects, without the need to access its namespace


# MODULARIZATION
# Practice of breaking a large application into smaller, reusable pieces
# The first executed module is called __main__

print()


# importing a module from the same directory as the working module - python knows the directory __main__ is and its subdirectories (not modules in directories above __main__)

import python_modules_example

print("This module: ", __name__)

print()
# to make other directories visible to __main__:
# (not an usual practice, modules should be under __main__'s reach)
sys.path.append("c:/dev/dev-intro/test/")

import testing_module  # module in the directory appended to sys.path

print(testing_module.testing_variable)
print()
# reloading modules:
# modules can be imported only once. to re-execute the module, import "importlib" and use importlib.realod(moduleName)
# it updates previously imported module (for interactive development, debugging, dynamic apps and plugins)

import importlib

for i in range(5):
    importlib.reload(testing_module)
    print()


# importing modules from packages (directories)
# import package_testing.test_package

# print(package_testing.test_package.pckg)

#  or: create a module __init__.py
import package_testing

print("\nprinting the package...")
print(package_testing.abc)
#  __init__.py makes the package to be considered a module
#  in this case, importing it with * inside the __init__.py module can be done! import all modules inside the package with *, so this can be done:

print(package_testing.pckg)
