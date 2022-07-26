from shape import Shape

class Rectangle(Shape):
    def __init__(self, id, location, color, width, length):
        super().__init__(id, location, color)
        self.width = width
        self.length = length

    def __str__(self):
        return super().__str__() + f', Width: {self.width}, Length: {self.length}'

    def get_area(self):
        return self.width * self.length