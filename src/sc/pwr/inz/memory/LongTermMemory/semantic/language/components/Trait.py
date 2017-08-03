
"""
Class representing Trait a.e Red,Elliptical
"""


class Trait:
    name = ""

    def __init__(self, name):
        """
        :param name (str): name of trait
        """
        self.name = name

    def gib_name(self):
        """
        :return: name of trait
        """
        return self.name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, Trait):
            return self.name.lower() == other.name.lower()

    def __hash__(self):
        return hash(self.name)
