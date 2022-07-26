from shape import Shape
from circle import Circle
from rectangle import Rectangle

c1 = Circle(id=1, location=(5, 3), color="Red", radius=2.5)
print(c1)
print("Area of c1:", c1.get_area())
c1.change_radius(5)
print("Area of c1:", c1.get_area())


r1 = Rectangle(id=2, location=(2, 4), color="Blue", width=5, length=10)
print(r1)
print("Area of r1:", r1.get_area())

shapes = [
    Circle(1, (2,3), "Black", 2.5),
    Rectangle(2, (5, 7), "Red", 10, 20),
    Circle(3, (4, 6), "Pink", 6.8)
]

total_area = 0
for shape in shapes:
    total_area += shape.get_area()  #in runtime, the specific version of get_area() will
                                    #be chosen according to the type of the shape
print(total_area)

#sum the areas of only the circles
total = 0
for shape in shapes:
    #if type(shape) is circle checks if the shape is of type circle and only circle,
    #not including subtypes
    if type(shape) is Circle:
        total += shape.get_area()

print("Total area of circles:", total)

total = 0
for shape in shapes:
    if isinstance(shape, Circle):
        total += shape.get_area()
print("Total area of circles:", total)

s = Shape(1, (3, 5), "Red")
print(s)