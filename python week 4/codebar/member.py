from abc import ABC

class Member(ABC):
    """Represents each member
    """
    def __init__(self, full_name):
        self.full_name = full_name

    def introduce(self):
        print(f'Hi, I\'m {self.full_name}!')

    