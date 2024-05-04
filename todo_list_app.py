from to_do_item_data import ToDoItemData
from typing import List

def add_todo_item(todo_item):
    todo_list.append(ToDoItemData(name=todo_item, is_checked=False))
    print("The to-do item has been added: " + todo_item)


def view_todo_list():
    print("\n")
    print("==============================")
    if not todo_list:
        print("no to-do list")
    else:
        for i, todo in enumerate(todo_list, start=1):
            print(f"[{todo.get_checked_icon_str()}] {i}. {todo.name} ")
    print("==============================")


def delete_todo_item(todo_item_no):
    try:
        removed_todo_item = todo_list.pop(int(todo_item_no) - 1)
        print("The to-do item has been deleted: " + removed_todo_item.name)
    except IndexError:
        print("The to-do item number cannot be found.")


def check_todo_item(todo_item_no):
    todo_list[int(todo_item_no) - 1].is_checked = True
    print("The to-do item has been checked: " + todo_list[int(todo_item_no) - 1].name)


def uncheck_todo_item(todo_item_no):
    todo_list[int(todo_item_no) - 1].is_checked = False
    print("The to-do item has been unchecked: " + todo_list[int(todo_item_no) - 1].name)


def main(action, todo_list):
    while action != '6':
        print("To-Do List Program starting...")
        print("1. Create a to-do item")
        print("2. View to-do items")
        print("3. Delete a to-do item")
        print("4. Check a to-do item")
        print("5. Uncheck a to-do item")
        print("6. Exit")

        action = input("Please enter the action you would like to execute: ")

        if action == '1':
            todo_item = input("Please enter the to-do item you would like to add: ")
            add_todo_item(todo_item)
        elif action == '2':
            view_todo_list()
        elif action == '3':
            todo_item_no = input("Please enter the to-do item number you would like to delete: ")
            delete_todo_item(todo_item_no)
        elif action == '4':
            todo_item_no = input("Please enter the to-do item number you would like to check: ")
            check_todo_item(todo_item_no)
        elif action == '5':
            todo_item_no = input("Please enter the to-do item number you would like to uncheck: ")
            uncheck_todo_item(todo_item_no)
        elif action == '6':
            print("To-Do List Program stoping...")
        else:
            print("Invalid action, please re-enter an action")

        print("\n")


if __name__ == '__main__':
    todo_list: list = []
    action = '0'
    main(action, todo_list)