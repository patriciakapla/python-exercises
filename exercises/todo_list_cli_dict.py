"""
Refactoring todo list:
Storing functions inside a dictionary so you can call them dynamically, using the dictionary method .get()
    Dynamic dispatch pattern
Storing results on json

"""

import json


def print_list(todo):
    if not todo:
        print("\nTasks:")
        print("- Empty list -")
    else:
        for i, task in enumerate(todo):
            print(f"{i + 1}. {task}")
    print()


def add_task(todo, removed):
    task = input("\nEnter a task: ")
    todo.append(task)
    print_list(todo)
    removed.clear()
    print()


def undo_task(todo, removed):
    if not todo:
        print("No tasks to undo!")
        return
    else:
        removed.append(todo.pop())
    print_list(todo)
    print()


def redo_task(todo, removed):
    if not removed:
        print("No tasks to redo!")
        return
    else:
        todo.append(removed.pop())
    print_list(todo)
    print()


def read_json(todo, file_path):
    data = []
    try:
        with open(file_path, "r", encoding="utf8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("File not found! Creating file...")
        save_json(todo, file_path)
    return data


def save_json(todo, file_path):
    data = todo
    with open(file_path, "w", encoding="utf8") as file:
        json.dump(todo, file, indent=2, ensure_ascii=False)
    return data


FILE_PATH = "todoList.json"
todo = read_json([], FILE_PATH)
removed = []
commands = {
    "list": lambda: print_list(todo),
    "add": lambda: add_task(todo, removed),
    "undo": lambda: undo_task(todo, removed),
    "redo": lambda: redo_task(todo, removed),
    "exit": "exit",
}

while True:
    print()
    print("Commands: list, add, undo, redo, exit")
    command = input("Enter a command or a task: ")

    action = (
        commands.get(command) if commands.get(command) is not None else commands["add"]
    )

    if action == "exit":
        break
    else:
        action()


save_json(todo, FILE_PATH)
