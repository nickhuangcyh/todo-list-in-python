from abc import ABC, abstractmethod

class Action:
    def __init__(self) -> None:
        pass

    @abstractmethod
    def execute(self, target_list):
        pass
    