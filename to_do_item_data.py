from dataclasses import dataclass

@dataclass
class ToDoItemData:
    name: str
    is_checked: bool

    def get_checked_icon_str(self):
        if self.is_checked:
            return "v"
        else:
            return " "