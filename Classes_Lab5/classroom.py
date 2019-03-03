class Classroom:
    """Class for classroom representation"""

    def __init__(self, number, capacity, equipment):
        """

        :param number: str
        :param capacity: int
        :param equipment: list

        Create new classroom

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_016.number
        '016'
        >>> classroom_016.capacity
        80
        >>> classroom_016.equipment
        ['PC', 'projector', 'mic']

        """
        self.number = number
        self.capacity = capacity
        self.equipment = equipment

    def __str__(self):
        """

        :return: str

        Return the information about class

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> print(classroom_016)
        Classroom 016 has a capacity of 80 persons and has the following equipment: PC, projector, mic.
        """
        return ("Classroom {} has a capacity of {} "
                "persons and has the following equipment: {}.").\
            format(self.number, str(self.capacity), ", ".join(self.equipment))

    def is_larger(self, classroom):
        """

        :param classroom: Classroom
        :return: bool

        Compares two classroms

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_016.is_larger(classroom_007)
        True
        """
        return self.capacity > classroom.capacity

    def equipment_differences(self, classroom):
        """

        :param classroom: Classroom
        :return: list

        Return the list of equipment
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_016.equipment_differences(classroom_007)
        ['PC', 'projector', 'mic']
        """

        return list(filter(lambda x: x not in classroom.equipment, self.equipment))

    def __repr__(self):
        """

        :return: str

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_016
        Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> [classroom_016]
        [Classroom('016', 80, ['PC', 'projector', 'mic'])]
        """

        return "Classroom{}".format(str((self.number, self.capacity, self.equipment)))
