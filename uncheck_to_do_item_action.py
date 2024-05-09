from action import Action
from to_do_item_data import ToDoItemData

class UncheckToDoItemAction(Action):
    def __init__(self):
        pass

    def execute(self, target_list):
        todo_item_no = input("Please enter the to-do item number you would like to check: ")
        target_list[int(todo_item_no) - 1].is_checked = False
        print("The to-do item has been checked: " + target_list[int(todo_item_no) - 1].name)
        