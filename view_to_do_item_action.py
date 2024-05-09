from action import Action
from to_do_item_data import ToDoItemData

class ViewToDoItemAction(Action):
    def __init__(self):
        pass

    def execute(self, target_list):
        print("\n")
        print("==============================")
        if not target_list:
            print("no to-do list")
        else:
            for i, todo in enumerate(target_list, start=1):
                print(f"[{todo.get_checked_icon_str()}] {i}. {todo.name} ")
        print("==============================")
        