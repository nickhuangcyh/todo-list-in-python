from action import Action
from to_do_item_data import ToDoItemData

class AddToDoItemAction(Action):
    def __init__(self):
        pass

    def execute(self, target_list):
        todo_item = input("Please enter the to-do item you would like to add: ")
        target_list.append(ToDoItemData(name=todo_item, is_checked=False))
        print("The to-do item has been added: " + todo_item)
        