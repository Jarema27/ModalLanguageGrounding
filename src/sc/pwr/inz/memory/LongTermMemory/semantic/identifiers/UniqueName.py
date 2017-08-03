from src.sc.pwr.inz.memory.LongTermMemory.semantic.identifiers.Identifier import Identifier

"""
Unique Name is identificator which base is string.
"""


class UniqueName(Identifier):

    name = ""

    def __init__(self, name):
        """
        :param name (str): unique name of certain identificator
        """
        self.name = name

    def get_code(self):
        """
        :return (str) unique name
        """
        return self.name

    def set_code(self, name):
        """
        :param name: new unique name
        """
        self.name = name

    def is_id_member_of(self):
        """
        Not implemented method,might be used in future
        :return:
        """
        return True

    def __str__(self):
        return "" + self.name + ""

    def __eq__(self, other):
        return self.name == other

    def __hash__(self):
        return hash(self.name)
