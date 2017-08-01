
from src.sc.pwr.inz.memory.semantic.KnowledgeBoosters.XMLReader import XMLReader

"""
Type of Object ,as example Tree is type of object, as well as Oak, so I might want to sit down to it and implement
self inheritance which would perfectly involve subtle beauty of diversity in our world
"""


class ObjectType:
    typeId = ""
    traits = []

    def __init__(self, id, traits):
        """
        :param id: Identifier : of that Object Type
        :param traits: list(Trait): set of Traits which given type can have
        """
        self.typeId = id
        self.traits = traits

    def get_type_id(self):
        """
        :return: Identifier: of this OT
        """
        return self.typeId

    def get_traits(self):
        """
        :return: traits which this OT can have
        """
        return self.traits

    def find_trait_by_name(self, name):
        """
        :param name: name of trait which we want to find
        :return: list of traits with such name
        """
        return list((x for x in self.traits if x.gib_name() == name))[0]

    def __eq__(self, other):
        return self.typeId == other.typeId

    @staticmethod
    def get_object_types():
        """
        Method using XMLReader to extract object types from XML File
        :return: list(ObjectType)
        """
        rot = XMLReader()
        desc = rot.read_object_types_xml()
        out = []
        for key in desc.keys():
            out += [ObjectType(key, desc.get(key))]
        return out

    def __str__(self):
        return str(self.typeId) + " " + str(self.traits)

    def __hash__(self):
        return hash(self.typeId)