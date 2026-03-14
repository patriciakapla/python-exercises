name = input('Enter your name: ')
age = input('Enter your age: ')

if not name or not age:
    print("You must enter both a name and age")
else:
    print(f'Your name is {name}')
    print(f'Your name reversed is {name[::-1]}')
    print(f"Your name has {len(name)} characters")
    print(f"The first letter of your name is {name[0]}")
    print(f"The last letter of yout name is {name[-1]}")
    if ' ' in name:
        print('Your name contains a space')
    else:
        print("Your name doesn't contain a space")
