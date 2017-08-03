import unittest

from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.ComplexFormula import ComplexFormula
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.Formula import TypeOfFormula
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.LogicalOperator import LogicalOperator
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.State import State

from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.Trait import Trait
from src.sc.pwr.inz.memory.LongTermMemory.semantic.IndividualModel import IndividualModel
from src.sc.pwr.inz.memory.LongTermMemory.semantic.ObjectType import ObjectType
from src.sc.pwr.inz.memory.LongTermMemory.semantic.identifiers.QRCode import QRCode


class ComplexFormulaTest(unittest.TestCase):

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

        self.cf1 = ComplexFormula(self.im1, [self.traits[0], self.traits[1]], [self.s2, self.s3], LogicalOperator.AND)
        self.cf2 = ComplexFormula(self.im2, [self.traits2[0], self.traits2[1]], [self.s1, self.s1], LogicalOperator.AND)

    def test_get_type(self):
        self.assertEqual(self.cf1.get_type(), TypeOfFormula.CF)
        self.assertEqual(self.cf2.get_type(), TypeOfFormula.CF)

    def test_get_states(self):
        self.assertEqual(self.cf1.get_states(), [self.s2, self.s3])
        self.assertEqual(self.cf2.get_states(), [self.s1, self.s1])

    def test_get_model(self):
        self.assertEqual(self.cf1.get_model(), self.im1)
        self.assertEqual(self.cf2.get_model(), self.im2)

    def test_get_traits(self):
        self.assertEqual(self.cf1.get_traits(), [self.traits[0], self.traits[1]])
        self.assertEqual(self.cf2.get_traits(), [self.traits2[0], self.traits2[1]])

    def test_eq(self):
        self.assertEqual(self.cf1, self.cf1)
        self.assertNotEqual(self.cf1, self.cf2)

    def test_get_complementary_formulas(self):
        self.assertEqual(self.cf1.get_complementary_formulas(), [ComplexFormula(self.im1, [self.traits[0], self.traits[1]],
                                                                           [self.s1, self.s1], LogicalOperator.AND),
                         ComplexFormula(self.im1, [self.traits[0], self.traits[1]], [self.s1, self.s2], LogicalOperator.AND),
                         ComplexFormula(self.im1, [self.traits[0], self.traits[1]], [self.s2, self.s1], LogicalOperator.AND),
                         ComplexFormula(self.im1, [self.traits[0], self.traits[1]], [self.s2, self.s2], LogicalOperator.AND)])

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
        self.cf1 = None
        self.cf2 = None
        self.s1 = None
        self.s2 = None
        self.s3 = None