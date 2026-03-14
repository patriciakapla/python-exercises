hour_input = input("Enter current hour: ")

try:
    hour = int(hour_input)
    if 0 <= hour <= 11:
        print("Good morning!")
    elif 12 <= hour <= 17:
        print("Good afternoon")
    elif 18 <= hour <= 23:
        print("Good evening")
    else:
        print("Enter a valid hour")
except:
        print("Enter a valid hour")
