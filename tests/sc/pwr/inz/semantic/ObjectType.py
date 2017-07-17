import unittest

from src.sc.pwr.inz.language.Trait import Trait
from src.sc.pwr.inz.memory.semantic.ObjectType import ObjectType


class ObjectTypeTest(unittest.TestCase):

    def setUp(self):
        self.traits = [Trait("Obly"),Trait("Krasny"),Trait("Sowiecki")]
        self.object_type = ObjectType(1,self.traits)
        self.traits2 = [Trait("Barowalny"),Trait("Konieczny"),Trait("Bolszoj")]
        self.object_type2 = ObjectType(2,self.traits2)

    def test_get_type_id(self):
        self.assertEquals(self.object_type.get_type_id(), 1)
        self.assertEquals(self.object_type2.get_type_id(), 2)

    def test_get_type_traits(self):
        self.assertEquals(self.object_type.get_traits()[1].gib_name(), "Krasny")
        self.assertEquals(self.object_type2.get_traits()[2].gib_name(), "Bolszoj")

    def test_find_trait_by_name(self):
        self.assertEquals(self.object_type.find_trait_by_name("Krasny"), self.traits[1])
        self.assertEquals(self.object_type2.find_trait_by_name("Bolszoj"), self.traits2[2])

    def tearDown(self):
        self.traits2 = None
        self.traits = None
        self.object_type = None
        self.object_type2 = None
