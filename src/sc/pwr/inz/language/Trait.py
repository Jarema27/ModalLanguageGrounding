
class Trait:
    name = ""

    def __init__(self,name):
        self.name = name

    def gib_name(self):
        return self.name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name.lower() == other.name.lower()

    def __hash__(self):
        return hash(self.name)