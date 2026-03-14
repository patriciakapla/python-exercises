first_name = input("Enter your first name: ")
name_length = len(first_name)
if name_length <= 4:
    print("Your name is short!")
elif 5 <= name_length <= 6:
    print("Your first name has a medium length")
elif name_length > 6:
    print("Your first name is long")