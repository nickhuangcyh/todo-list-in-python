from action import Action
from to_do_item_data import ToDoItemData

class DeleteToDoItemAction(Action):
    def __init__(self):
        pass

    def execute(self, target_list):
        todo_item_no = input("Please enter the to-do item number you would like to delete: ")
        try:
            removed_todo_item = target_list.pop(int(todo_item_no) - 1)
            print("The to-do item has been deleted: " + removed_todo_item.name)
        except IndexError:
            print("The to-do item number cannot be found.")
        