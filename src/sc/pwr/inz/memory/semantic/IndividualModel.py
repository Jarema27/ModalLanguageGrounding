"""
Module which is embodiment of specific object spotted in the world. As example Oak is object type, while Oak Bartek
is instance of Oak as well as Individual Model in our memory.
We could say that biblical Adam was XML Parser who established object types of animals, while every other human could
call his instance of animal any name he wished.
In addition every object type has certain set of traits agent associates it with.
"""


class IndividualModel:
    identifier = None
    object_type = None

    def __init__(self, idn, ot):
        """
        :param idn (Identifier): which we use to tell difference between two Individual Models
        :param ot (ObjectType): type of that object a.e Fish
        """
        self.identifier = idn
        self.object_type = ot

    def get_identifier(self):
        """
        :return: Identifier: of this IM
        """
        return self.identifier

    def get_object_type(self):
        """
        :return: ObjectType : of this IM
        """
        return self.object_type

    def set_identifier(self, idn):
        """
        :param idn: Identifier: we'd like to set
        """
        self.identifier = idn

    def set_object_type(self, ot):
        """
        :param ot: ObjectType we'd like to set
        """
        self.object_type = ot

    def check_if_contains_traits(self, traits):
        """
        Determines if IM's ObjectType involved given traits
        :param traits: traits to test
        :return: Boolean: True when trait is in object_type,False otherwise
        """
        for x in traits:
            if x not in self.object_type.get_traits():
                return False
        return True

    def __eq__(self, other):
        return self.identifier.get_code() == other.identifier.get_code()

    def __str__(self):
        return "IndividualModel{" + "identifier=" + str(self.identifier) + "}"

    def __hash__(self):
        return hash(self.identifier) * hash(self.object_type)
