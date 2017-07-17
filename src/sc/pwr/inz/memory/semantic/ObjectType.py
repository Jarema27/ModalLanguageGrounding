

class ObjectType:
    typeId = ""
    traits = []

    def __init__(self, id, traits):
        self.typeId = id
        self.traits = traits

    def get_type_id(self):
        return self.typeId

    def get_traits(self):
        return self.traits

    def find_trait_by_name(self, name):
        return list((x for x in self.traits if x.gib_name() == name))[0]

    def __eq__(self, other):
        return self.typeId == other.typeId

    @staticmethod
    def get_object_types():
        #todo
        return ["01", "02", "03"]

    def __str__(self):
        return str(self.typeId) + " " + str(self.traits)
