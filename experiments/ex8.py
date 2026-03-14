string = "Lion, Mulan e Zé"
counter = 0
i = 0
new_string = ""


while counter < len(string):
    new_string += "*" + string[i]
    i += 1
    counter += 1

print(new_string)