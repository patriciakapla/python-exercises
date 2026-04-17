"""
TO DO LIST
Functionalities:
- add item
- undo
- redo
- list items
"""


def ask_command():
    print(
        "Commands: \n \
        [1] List \n \
        [2] New task \n \
        [3] Undo \n \
        [4] Redo \n \
        [0] Exit"
    )
    try:
        command = int(input("Enter command number: "))
    except ValueError:
        print("Must enter a number.")
        command = None
    print()
    return command


def print_list(todo_list):
    if not todo_list:
        print("No tasks on the list!")
        print()

    else:
        print("Tasks:")
        for index, task in enumerate(todo_list):
            print(f"{index + 1}. {task}")
        print()


def new_task(todo_list, removed_list):
    item = input("Enter the task: ")
    print(f'\n"{item}" added to list \n')
    todo_list.append(item)
    print_list(todo)
    print()
    removed_list.clear()


def undo(removed_list, todo_list):
    try:
        removed_list.append(todo_list.pop())
        item = removed_list[-1]
        print(f'\n"{item}" removed from list\n')
        print_list(todo)
        print()

    except IndexError:
        print("No tasks left to undo!")
        print()


def redo(removed_list, todo_list):
    try:
        todo_list.append(removed_list.pop())
        item = todo_list[-1]
        print(f'\n"{item}" added to list\n')
        print_list(todo)
        print()
    except IndexError:
        print("No tasks left to redo!")
        print()


todo = []
removed = []
# MAIN PROGRAM

while True:
    command = ask_command()
    if command is None:
        continue

    match command:
        case 1:
            print_list(todo)
        case 2:
            new_task(todo, removed)
        case 3:
            undo(removed, todo)
        case 4:
            redo(removed, todo)
        case 0:
            print("Leaving...")
            break
        case _:
            print("Invalid command")
