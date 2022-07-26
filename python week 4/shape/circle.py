from shape import Shape
import math
#inheritance example, shape = base class, circle = subclass

class Circle(Shape):
    """A circle shape
    """
    #attributes of shape automatically add to attributes of circle
    #also need to get additional attributes of circle: radius
    def __init__(self, id, location, color, radius):
        #super is like self, prevents recursion between classes
        #need to use super keyword to use base class methods 

        #callign the super class init method to initialize the attributes of Shape
        super().__init__(id, location, color)
        #add any specific attributes of the subclass
        self.radius = radius

    #overriding the string implementation inherited from Shape
    #doing this because we need to add radius info
    def __str__(self):
        return super().__str__() + f', Radius: {self.radius}'

    def get_area(self):
        #area of a circle: pi(r)**2
        return math.pi * self.radius ** 2

    def draw(self):
        pass

    #new method added to the subclass
    def change_radius(self, new_radius):
        self.radius = new_radius