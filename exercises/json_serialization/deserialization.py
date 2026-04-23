"""
Deserialize Character objects from a JSON file.

Reads JSON data, reconstructs Character instances, and prints them.
"""

import json
from serialization import FILE_PATH, Character


with open(FILE_PATH, "r", encoding="utf8") as file:
    characters = json.load(file)


character1 = Character(**characters[0])
character2 = Character(**characters[1])
character3 = Character(**characters[2])
character4 = Character(**characters[3])
character5 = Character(**characters[4])


print(character1, character2, character3, character4, character5)
