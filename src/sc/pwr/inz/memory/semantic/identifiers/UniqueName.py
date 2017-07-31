from src.sc.pwr.inz.memory.semantic.identifiers.Identifier import Identifier


class UniqueName(Identifier):

    name = ""

    def __init__(self, name):
        self.name = name

    def get_code(self):
        return self.name

    def set_code(self, name):
        self.name = name

    def is_id_member_of(self):
        return True

    def __str__(self):
        return "" + self.name + ""

    def __eq__(self, other):
        return self.name == other

    def __hash__(self):
        return hash(self.name)
