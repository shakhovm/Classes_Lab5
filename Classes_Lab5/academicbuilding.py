from Classes_Lab5 import classroom
from collections import Counter


class AcademicBuilding:
    """Class Academic Building"""
    def __init__(self, address, classrooms):
        """

        :param address: str
        :param classrooms: list


        >>> classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = classroom.Classroom('007', 12, ['TV'])
        >>> classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> building.address
        'Kozelnytska st. 2a'
        """

        self.address = address
        self.classrooms = classrooms

    def total_equipment(self):
        """

        :return: list

        Return the total equipment in building
        >>> classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = classroom.Classroom('007', 12, ['TV'])
        >>> classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> building.total_equipment()
        [('PC', 2), ('TV', 1), ('mic', 1), ('projector', 2)]
        """
        all_equipments = ",".join(list(map(lambda element: ",".join(element),
                                           [classroom.equipment for classroom in self.classrooms]))).split(',')
        return sorted([equip for equip in Counter(all_equipments).items()])

    def __str__(self):
        """

        :return: str

        >>> classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = classroom.Classroom('007', 12, ['TV'])
        >>> classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> print(building)
        Kozelnytska st. 2a
        Classroom 016 has a capacity of 80 persons and has the following equipment: PC, projector, mic.
        Classroom 007 has a capacity of 12 persons and has the following equipment: TV.
        Classroom 008 has a capacity of 25 persons and has the following equipment: PC, projector.

        """
        return "{}\n{}".format(self.address, "\n".join([classroom.__str__() for classroom in self.classrooms]))



