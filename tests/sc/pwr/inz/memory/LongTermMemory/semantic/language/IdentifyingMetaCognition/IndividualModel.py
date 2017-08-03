import unittest

from src.sc.pwr.inz.memory.LongTermMemory.semantic.IdentifyingMetaCognition.IndividualModel import IndividualModel
from src.sc.pwr.inz.memory.LongTermMemory.semantic.IdentifyingMetaCognition.ObjectType import ObjectType
from src.sc.pwr.inz.memory.LongTermMemory.semantic.identifiers.QRCode import QRCode
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.Trait import Trait


class TestIndividualModel(unittest.TestCase):

    def setUp(self):
        self.ident1 = QRCode("1")
        self.ident2 = QRCode("2")
        self.ident3 = QRCode("-231")

        self.traits = [Trait("Obly"),Trait("Krasny"), Trait("Sowiecki")]
        self.object_type = ObjectType(1, self.traits)
        self.traits2 = [Trait("Barowalny"), Trait("Konieczny"), Trait("Bolszoj")]
        self.object_type2 = ObjectType(2, self.traits2)

        self.im1 = IndividualModel(self.ident1, self.object_type)
        self.im2 = IndividualModel(self.ident2, self.object_type2)

    def test_get_identifier(self):
        self.assertEquals(self.im1.get_identifier(), self.ident1)
        self.assertEquals(self.im2.get_identifier(), self.ident2)
        self.assertNotEquals(self.im2.get_identifier(), self.ident3)

    def test_get_object_type(self):
        self.assertEquals(self.im1.get_object_type(), self.object_type)
        self.assertEquals(self.im2.get_object_type(), self.object_type2)

    def test_set_identifier(self):
        self.im1.set_identifier(self.ident3)
        self.assertEquals(self.im1.get_identifier(), self.ident3)
        self.im2.set_identifier(self.ident1)
        self.assertEquals(self.im2.get_identifier(), self.ident1)

    def test_set_object_type(self):
        self.im1.set_object_type(self.object_type2)
        self.im2.set_object_type(self.object_type)
        self.assertEquals(self.im1.get_object_type(), self.object_type2)
        self.assertEquals(self.im2.get_object_type(), self.object_type)

    def test_check_if_contains_traits(self):
        self.assertTrue(self.im1.check_if_contains_traits([self.traits[0]]))
        self.assertTrue(self.im2.check_if_contains_traits([self.traits2[1], self.traits2[2]]))
        self.assertFalse(self.im1.check_if_contains_traits([self.traits2[1]]))

    def test_equals(self):
        self.assertFalse(self.im1 == self.im2)
        self.assertTrue(self.im1 == self.im1)
        im3 = IndividualModel(self.ident1, self.object_type)
        self.assertEquals(self.im1,im3)

    def tearDown(self):
        self.traits2 = None
        self.traits = None
        self.object_type = None
        self.object_type2 = None
        self.ident1 = None
        self.ident2 = None
        self.ident3 = None
        self.im1 = None
        self.im2 = None
