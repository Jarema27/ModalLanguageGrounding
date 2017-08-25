
from src.sc.pwr.inz.memory.LongTermMemory.semantic.KnowledgeBoosters.XMLReader import XMLReader

"""
Type of Object ,as example Tree is type of object, as well as Oak, so I might want to sit down to it and implement
self inheritance which would perfectly involve subtle beauty of diversity in our world
"""


class ObjectType:
    typeId = ""
    traits = []

    def __init__(self, id, traits, superphylium=None, infraphylium=None, cluster=None):
        """
        :param id: Identifier : of that Object Type
        :param superphylium: ObjectType or list(ObjectType): sphere of OT which are superior to this one
        :param infraphylium: ObjectType or list(ObjectType): sphere of OT which are inferior to this one
        :param cluster: list(Cluster) : list of  clusters this OT belongs to (might be of length equal to one)
        :param traits: list(Trait): set of Traits which given type can have
        """
        self.typeId = id
        if superphylium is not None:
            self.superphylium = superphylium
        else:
            self.superphylium = []
        if infraphylium is not None:
            self.infraphylium = infraphylium
        else:
            self.infraphylium = []
        if cluster is None:
            self.cluster = []
        else:
            self.cluster = cluster
        self.traits = traits

    def get_type_id(self):
        """
        :return Identifier: of this OT
        """
        return self.typeId

    def get_cluster(self):
        """
        :return list(Cluster):List of clusters this OT belongs to
        """
        return self.cluster

    def get_superphylium(self):
        """
        :return ObjectType or list(ObjectType): all OT superior to this one
        """
        return self.superphylium

    def get_infraphylium(self):
        """
        :return ObjectType or list(ObjectType): all OT inferior to this one
        """
        return self.infraphylium

    def add_superior(self, typ):
        """
        :param typ : ObjectType we want to append to superphylium
        """
        self.superphylium.append(typ)

    def add_inferior(self,typ):
        """
        :param typ: ObjectType we want to append to infraphylium
        """
        self.infraphylium.append(typ)

    def get_traits(self):
        """
        :return traits which this OT can have
        """
        return self.traits

    def set_cluster(self, cluster):
        """
        :param cluster: list(Cluster) which will be new list of clusters this OT belongs to
        """
        self.cluster = cluster

    def get_traits_all_the_way_up(self):
        """
        :return list(Traits): All traits from superior OT with traits of this OT.
        """
        out = self.traits
        for superior in self.superphylium:
            out = out + (superior.get_traits_all_the_way_up())
        return out

    def find_trait_by_name(self, name):
        """
        :param name: name of trait which we want to find
        :return list of traits with such name
        """
        return list((x for x in self.traits if x.gib_name() == name))[0]

    def __eq__(self, other):
        return self.typeId == other.typeId

    @staticmethod
    def get_object_types():
        """
        Method using XMLReader to extract object types from XML File
        :return list(ObjectType)
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
