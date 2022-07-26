from abc import ABC, abstractmethod

class Shape():
    """A general base class for representing any type of shape
    """

    def __init__(self, id, location, color):
        self.id = id
        self.location = location
        self.color = color

    @abstractmethod
    def get_area(self):
        """Returns the area of the shape (not implemented in the base case)
        """
        pass

    def draw(self):
        """Draw the shape on the screen (not implemented now)
        """
        pass

    def change_location(self, new_location):
        self.location = new_location

    def __str__(self):
        return f'Id: {self.id}, Location: {self.location}, Color: {self.color}'

        