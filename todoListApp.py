todo_list = []
action = '0'

def add_todo_item(todo_item):
    todo_list.append(todo_item)
    print("The to-do item has been added: " + todo_item)

def view_todo_list():
    print("\n")
    print("==============================")
    if not todo_list:
        print("no to-do list")
    else:
        for i, todo in enumerate(todo_list, start=1):
            print(f"{i}. {todo}")
    print("==============================")

def delete_todo_item(todo_item_no):
    try:
        removed_todo_item = todo_list.pop(int(todo_item_no) - 1)
        print("The to-do item has been deleted: " + removed_todo_item)
    except IndexError:
        print("The to-do item number cannot be found.")

def main(action, todo_list):
    while action != '4':
        print("To-Do List Program starting...")
        print("1. Create a to-do item")
        print("2. View to-do items")
        print("3. Delete a to-do item")
        print("4. Exit")

        action = input("Please enter the action you would like to execute: ")

        if action == '1':
            todo_item = input("Please enter the to-do item you would like to add: ")
            add_todo_item(todo_item)
        elif action == '2':
            view_todo_list()
        elif action == '3':
            todo_item = input("Please enter the to-do item you would like to delete: ")
            delete_todo_item(todo_item)
        elif action == '4':
            print("To-Do List Program stoping...")
        else:
            print("Invalid action, please re-enter an action")

        print("\n")

if __name__ == '__main__':
    main(action, todo_list)