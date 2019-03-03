from Classes_Lab5.triangle import Triangle
from Classes_Lab5 import point

triangle = Triangle(point.Point(1, 1), point.Point(3, 1), point.Point(2, 3))
print(triangle.is_triangle())
print(triangle.perimeter())
print(triangle.area())

