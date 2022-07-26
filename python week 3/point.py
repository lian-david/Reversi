#ex of how to define a class

class Point: 
    """This class represents a two-dimensional point with (x, y) coordinates
    """
    def __init__(self, x, y):
        """Initializes the x and y coordinates of the point

        Args:
            x(int): x coordinate
            y(int): y coordinate 
        """
        self.x = x
        self.y = y 

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def __str__(self):
        return f'({self.x}, {self.y})'

    #operator overloading:

    def __add__(self, other):
        #enables user to add new points together in a new point/variable
        #use class to create new point of sum
        #enable adding ints if type is not point
        if type(other) is Point:
            return Point(self.x + other.x, self.y + other.y)
        elif type(other) is int:
            return Point(self.x + other, self.y + other)
        else:
            raise TypeError("Type is not supported.")

    def __radd__(self, other):
        if type(other) is int:
            return Point(self.x + other, self.y + other)

    def __sub__(self, other):
        #subtract 2 points
        return Point(self.x - other.x, self.y - other.y)

    def __lt__(self, other):
        #returns boolean if point is less than other
        return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)
        
        
#you typically don't define objects in same place where you define class

#this creates 2 instances (p1, p2) of the same class where each has its own space in 
#memory and each has its own attributes 

p1 = Point(2, 5)
print(p1.x, p1.y)

p2 = Point(3,6)
print(p2.x, p2.y)

p1.move(4, 4)
print(p1.x, p1.y)

print("P1:", p1)
print("P2:", p2)

p3 = p1 + p2
print("P3:", p3)

p4 = p1 - p2
print("P4:", p4)

print(p3 < p4)

p5 = Point(1, 5)
p6 = Point(1, 5)
print(p5 == p6)         #returns False bc/ these are 2 different objects in memory, 
                        #returns True after operator overload

p7 = p5 + 2
print("P7:", p7)

p8 = 2 + p5
print("P8:", p8)