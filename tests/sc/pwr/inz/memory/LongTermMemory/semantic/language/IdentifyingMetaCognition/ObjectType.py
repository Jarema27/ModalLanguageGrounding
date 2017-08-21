import unittest

from src.sc.pwr.inz.memory.LongTermMemory.semantic.IdentifyingMetaCognition.Cluster import Cluster
from src.sc.pwr.inz.memory.LongTermMemory.semantic.IdentifyingMetaCognition.ObjectType import ObjectType
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.Trait import Trait


class ObjectTypeTest(unittest.TestCase):

    def setUp(self):
        self.traits = [Trait("Obly"), Trait("Krasny"), Trait("Sowiecki")]
        self.object_type = ObjectType(1, self.traits)
        self.traits2 = [Trait("Barowalny"), Trait("Konieczny"), Trait("Bolszoj")]
        self.object_type2 = ObjectType(2, self.traits2)

        self.cl1 = Cluster("Płaz", self.traits)
        self.object_type3 = ObjectType(3, self.traits2, [self.object_type], [self.object_type2])
        self.object_type4 = ObjectType(4, self.traits2, [self.object_type3], [self.object_type2], self.cl1)

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

    def test_get_cluster(self):
        self.assertEqual(self.object_type4.get_cluster(), self.cl1)

    def test_get_superphylium(self):
        self.assertEqual(self.object_type4.get_superphylium(), [self.object_type3])
        self.assertEqual(self.object_type3.get_superphylium(), [self.object_type])
        self.assertEqual(self.object_type2.get_superphylium(), [])

    def test_get_infraphylium(self):
        self.assertEqual(self.object_type4.get_infraphylium(), [self.object_type2])
        self.assertEqual(self.object_type3.get_infraphylium(), [self.object_type2])
        self.assertEqual(self.object_type2.get_infraphylium(), [])

    def test_get_traits_all_the_way_up(self):
        self.assertEqual(self.object_type.get_traits_all_the_way_up(), self.traits)
        self.assertEqual(self.object_type2.get_traits_all_the_way_up(), self.traits2)
        self.assertEqual(len(self.object_type3.get_traits_all_the_way_up()), len(self.traits + self.traits2))
        self.assertEqual(len(self.object_type4.get_traits_all_the_way_up()), len(self.traits + self.traits2*2))

    def tearDown(self):
        self.traits2 = None
        self.traits = None
        self.object_type = None
        self.object_type2 = None
