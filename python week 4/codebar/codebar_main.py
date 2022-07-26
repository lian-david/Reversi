from student import Student
from instructor import Instructor
from workshops import Workshop

workshop = Workshop("12/03/2021", "Programming in Python")

jane = Student("Jane Doe", "I'm trying to learn programming and need some help")
lena = Student("Lena Smith", "I'm really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding")
vicky.add_skill("Python")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I've been coding in Python for 5 years")
nicole.add_skill("Python")

workshop.add_participants(jane)
workshop.add_participants(lena)
workshop.add_participants(vicky)
workshop.add_participants(nicole)
workshop.print_details()