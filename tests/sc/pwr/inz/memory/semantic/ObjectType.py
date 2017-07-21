import unittest

from src.sc.pwr.inz.language.components.Trait import Trait
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

    def test_get_object_types(self):
        self.assertEqual(ObjectType.get_object_types()[0], ObjectType('1', [Trait("Red"), Trait("Bolszoj")]))
        self.assertEqual(ObjectType.get_object_types()[1], ObjectType('2', [Trait("Red"), Trait("Bolszoj")]))
        self.assertEqual(ObjectType.get_object_types()[2], ObjectType('3', [Trait("Red"), Trait("Bolszoj")]))

        self.assertEqual(ObjectType.get_object_types()[1], ObjectType('2', [Trait("Juicy")]))

        self.assertEqual(ObjectType.get_object_types()[2], ObjectType('3', [Trait("Bloody"), Trait("Twisted")]))
        self.assertEqual(ObjectType.get_object_types(), [ObjectType('1', [Trait("Red"), Trait("Bolszoj")])
                                                         , ObjectType('2', [Trait("Juicy")])
                                                         , ObjectType('3', [Trait("Bloody"), Trait("Twisted")])])

    def tearDown(self):
        self.traits2 = None
        self.traits = None
        self.object_type = None
        self.object_type2 = None
