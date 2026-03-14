number = input("Enter a whole number: ")
try:
    number_int = int(number)
    if number_int % 2 == 0:
        print(f"{number_int} is even")
    else:
        print(f"{number_int} is odd")
except:
    print("Please enter a whole number")
