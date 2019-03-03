from math import sqrt
from Classes_Lab5 import line, point


class Triangle:
    """
    Triangle
    """
    def __init__(self, top_a, top_b, top_c):
        """

        :param top_a: Point
        :param top_b: Point
        :param top_c: Point

        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
        >>> triangle.side_ab
        2.0
        """
        self.top_a = top_a
        self.top_b = top_b
        self.top_c = top_c
        self.side_ab = line.Line(self.top_a, self.top_b).line
        self.side_ac = line.Line(self.top_a, self.top_c).line
        self.side_bc = line.Line(self.top_b, self.top_c).line

    def is_triangle(self):
        """

        :return: bool

        Check if it is a triangle

        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
        >>> triangle.is_triangle()
        True
        """
        return (self.side_ab + self.side_ac > self.side_bc) and \
               (self.side_ac + self.side_bc > self.side_ab) and \
               (self.side_ab + self.side_bc > self.side_ac)

    def perimeter(self):
        """

        :return: float

        Return perimeter of the triangle

        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
        >>> triangle.perimeter()
        6.47213595499958
        """
        return self.side_ab + self.side_ac + self.side_bc

    def area(self):
        """

        :return: float

        Return area of the triangle

        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
        >>> triangle.area()
        2.0
        """
        halfp = self.perimeter()/2
        return sqrt(halfp*(halfp - self.side_ab)*(halfp - self.side_ac)*(halfp - self.side_bc))


