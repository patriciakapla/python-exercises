"""
FILE HANDLING

open()
    opens file
    can create a file by opening it

MODES
r (reading)
w (writing) - overwrites whatever content
x (creating) - exclusively for creating. not much used
a (appends to end)
b (binary)
t (text)
+ (adds functionality!) - r+ or w+ (reading + writing)


WHEN OPENING A FILE, ALWAYS CLOSE IT AFTER!
    file.close()

FILE PATH:
if you dont specify the path to the new file, it'll be created in the working folder:
    "new_file.txt"
mac/linux:
    use full path.
    ex: /Users/name/desktop/somefolder
windows:
    paths use backslash!  which is a problem because python uses backslash for escaping!
    so, when using paths with backslash, use 2 instead of one!
    ex: C:\\Users\\Patricia\\Tropidark\\Projetos


CONTEXT MANAGER
opens and closes files automatically


"""

file_path = "./experiments/new_file.txt"

# file = open(file_path, "r")  # FileNotFoundError !!!!
# in this case throws an error, since reading doesn't create the file!
# to create the file, use one of the writing modes (w, a), or the creating mode (x):

# file = open(file_path, "w")

# file.close()


# can be done with try/except:
try:
    print("Reading file...")
    file = open(file_path, "r")
    print("File ready!")
except FileNotFoundError:
    print("File not found!")
    print("Creating file...")
    file = open(file_path, "w")
    print("File created succesfully!")
finally:
    print("Closing file...")
    file.close()
    print("File closed")

# CONTEXT MANAGER
# opens and closes file automatically!
# using WITH syntax:
print()
with open(file_path, "w") as file:
    print("opening file...")
    print("closing file...")

print()

# WRITING and READING / useful modes and methods

# with open(file_path, "w") as file:
#     file.write("Line 1\n")
#     file.write("Line 2\n")
#     file.write("Line 3\n")
#     file.write("Line 4\n")

# with open(file_path, "r") as file:
#     print(file.read())
print()

with open(file_path, "w+") as file:
    print(type(file))
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Now writing AND reading \n")
    # print(file.read())          #NOT READING! after writing, "cursor" is at the end of the file - nothing to read

    file.seek(0, 0)  # returns cursor to the top of the archive, so it can be read

    print(file.read())  # now it can be read!

    file.writelines(("Line 4\n", "Line 5\n"))

    file.seek(0, 0)
    print(file.readline(), end="")  # like next, every execution returns next line.
    print(file.readline())

    file.seek(0, 0)

    print("readlinesssss")
    for line in file.readlines():
        print(line, end="")


with open(file_path, "a+") as file:
    file.write("Appended line\n")
    file.seek(0, 0)
    print(file.read())


# Character table might be different. windows doesnt use UTF-8, so many characters are not read. (see new_file.txt)

with open(file_path, "a+") as file:
    file.write("Atenção!\n")  # (see new_file.txt)

# in this case, encoding is necessary:

with open(file_path, "a+", encoding="utf8") as file:
    file.write("Atenção!\n")  # (see new_file.txt)


# os.remove or unlike erases the file
import os

# os.remove(file_path)
# os.unlike(file_path)

#  os.rename renames file:

os.rename(file_path, "./experiments/file_handling_test.txt")
