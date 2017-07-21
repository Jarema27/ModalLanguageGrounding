import unittest
from src.sc.pwr.inz.language.Trait import Trait
from src.sc.pwr.inz.memory.semantic.ObjectType import ObjectType
from src.sc.pwr.inz.memory.semantic.identifiers.QRCode import QRCode
from src.sc.pwr.inz.memory.semantic.IndividualModel import IndividualModel
from src.sc.pwr.inz.language.State import State
from src.sc.pwr.inz.language.SimpleFormula import SimpleFormula
from src.sc.pwr.inz.language.Formula import TypeOfFormula


class SimpleFormulaTest(unittest.TestCase):

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

        self.s1 = State.IS
        self.s2 = State.IS_NOT
        self.s3 = State.MAYHAPS

        self.sf1 = SimpleFormula(self.im1, self.traits[1], self.s1)
        self.sf3 = SimpleFormula(self.im2, self.traits2[2], self.s2)

    def test_get_states(self):
        self.assertEquals(self.sf1.get_states(), [self.s1])
        self.assertEquals(self.sf3.get_states(), [self.s2])

    def test_error(self):
        self.assertRaises(TypeError, lambda: SimpleFormula(self.im1, [self.traits[1]], self.s1))

    def test_get_model(self):
        self.assertEqual(self.sf1.get_model(), self.im1)
        self.assertNotEqual(self.sf1.get_model(), self.im2)

    def test_test_get_type(self):
        self.assertEqual(self.sf1.get_type(), TypeOfFormula.SF)
        self.assertEqual(self.sf3.get_type(), TypeOfFormula.SF)

    def test_get_complementary_formulas(self):
        self.assertEqual(self.sf1.get_complementary_formulas(), [SimpleFormula(self.im1, self.traits[1],
                                                                               self.s1),
                                                                 SimpleFormula(self.im1, self.traits[1],
                                                                 self.s2)])
        self.assertEqual(self.sf3.get_complementary_formulas(), [SimpleFormula(self.im2, self.traits2[2],
                                                                               self.s1),
                                                                 SimpleFormula(self.im2, self.traits2[2],
                                                                 self.s2)])

    def test_eq(self):
        self.assertEqual(self.sf1, SimpleFormula(self.im1, self.traits[1], self.s1))
        self.assertEqual(self.sf3, SimpleFormula(self.im2, self.traits2[2], self.s2))

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
        self.sf1 = None
        self.sf2 = None
        self.s1 = None
        self.s2 = None
        self.s3 = None
