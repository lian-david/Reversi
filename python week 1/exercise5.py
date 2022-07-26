#this doesnt work? not sure
import math
q1 = float(input("Enter the first coefficient:"))
q2 = float(input("Enter the second coefficient:"))
q3 = float(input("Enter the third coefficient:"))

quad = math.sqrt(q2 ** 2 - 4 * q1 * q3)
ans1 = (-q2-quad) / (2 * q1)
ans2 = (-q2+quad) / (2 * q1)
print("The solutions to the quadratic equation are: ", ans1, "and", ans2)

