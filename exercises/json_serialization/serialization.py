"""
Serialize Character objects into a JSON file.

Defines the Character class, creates sample instances, and writes their
data as a list of dictionaries to disk.
"""

import json

FILE_PATH = "./exercises/json_serialization/data.json"


class Character:
    def __init__(self, name: str, hunter: bool, vampire: bool) -> None:
        self.name = name
        self.hunter = hunter
        self.vampire = vampire


character1 = Character("Buffy Summers", True, False)
character2 = Character("Angel", False, True)
character3 = Character("Willow Rosenberg", True, False)
character4 = Character("Spike", False, True)
character5 = Character("Drusilla", False, True)


if __name__ == "__main__":

    characters = [
        character1.__dict__,
        character2.__dict__,
        character3.__dict__,
        character4.__dict__,
        character5.__dict__,
    ]

    with open(FILE_PATH, "w", encoding="utf8") as file:
        json.dump(characters, file, ensure_ascii=False, indent=1)
