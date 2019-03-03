from Classes_Lab5 import point


class Line:
    """
    Line
    """
    def __init__(self, point_1, point_2):
        """

        :param point_1: Point
        :param point_2: Point

        >>> l = Line(point.Point(1, 1), point.Point(2, 2))
        >>> l.line
        1.4142135623730951
        """
        self.point_1 = point_1
        self.point_2 = point_2
        self.line = ((self.point_1.position[0] - self.point_2.position[0])**2 +
                     (self.point_1.position[1] - self.point_2.position[1])**2)**0.5

