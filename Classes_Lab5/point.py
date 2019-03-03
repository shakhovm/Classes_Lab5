class Point:
    """
    Point
    """
    def __init__(self, x, y):
        """

        :param x: float
        :param y: float

        >>> p = Point(1, 1)
        >>> p.position
        (1, 1)
        """
        self.x = x
        self.y = y
        self.position = self.x, self.y


