"""
JSON - javascript object notation

Data structure created to store and transfer data
Similar to python's dictionary
Looks like a javascript object
data types:
    boolean
    number (int, float)
    null
    string
    array []
    object {}

not supported: functions, methods, classes, sets

json is used to transmitting data from servers and other apps
"""

import json
import os

person = {
    "name": "Willian",
    "last_name": "Brito Piovezan",
    "nickname": "Bitelo",
    "height": 2.02,
    "weight": 138,
    "PRs": {"bench": 202.5, "deadlift": 390, "squat": 340},
}


# with open("./notes/json_example.json", "w", encoding="utf8") as file:
#     json.dump(person, file, ensure_ascii=False, indent=2)

#  THE CODE ABOVE WROTE A JSON FILE WITH THE PERSON DICTIONARY.
#  THE FOLLOWING CODE IS HOW TO GET DATA FROM A JSON FILE. I'll use the same json file, so it will put the data in json into new_person

with open("./notes/json_example_3.json", "r", encoding="utf8") as file:
    new_person = json.load(file)
    print(new_person)
    print(type(new_person))
    print(new_person["PRs"])
