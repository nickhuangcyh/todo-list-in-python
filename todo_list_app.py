from add_to_do_item_action import AddToDoItemAction
from view_to_do_item_action import ViewToDoItemAction
from delete_to_do_item_action import DeleteToDoItemAction
from check_to_do_item_action import CheckToDoItemAction
from uncheck_to_do_item_action import UncheckToDoItemAction

def main(action, target_list):
    actions = {
        '1': AddToDoItemAction(),
        '2': ViewToDoItemAction(),
        '3': DeleteToDoItemAction(),
        '4': CheckToDoItemAction(),
        '5': UncheckToDoItemAction()
    }

    while True:
        print("To-Do List Program starting...")
        print("1. Create a to-do item")
        print("2. View to-do items")
        print("3. Delete a to-do item")
        print("4. Check a to-do item")
        print("5. Uncheck a to-do item")

        action = input("Please enter the action you would like to execute: ")

        if action in actions:
            actions[action].execute(target_list)
        else:
            print("Invalid action, please re-enter an action")

        print("\n")


if __name__ == '__main__':
    todo_list: list = []
    action = '0'
    main(action, todo_list)
    