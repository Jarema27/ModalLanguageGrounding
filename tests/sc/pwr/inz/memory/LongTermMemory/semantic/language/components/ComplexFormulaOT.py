import unittest

from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.ComplexFormulaOT import ComplexFormulaOT
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.LogicalOperator import LogicalOperator
from src.sc.pwr.inz.memory.LongTermMemory.semantic.IdentifyingMetaCognition.ObjectType import ObjectType
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.State import State
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.Trait import Trait
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.Formula import TypeOfFormula
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.Tense import Tense


class ComplexFormulaOTTest(unittest.TestCase):

    def setUp(self):
        self.traits = [Trait("Obly"), Trait("Krasny"), Trait("Sowiecki")]
        self.object_type = ObjectType(1, self.traits)
        self.traits2 = [Trait("Barowalny"), Trait("Konieczny"), Trait("Bolszoj")]
        self.object_type2 = ObjectType(2, self.traits2)

        self.s1 = State.IS
        self.s2 = State.IS_NOT
        self.s3 = State.MAYHAPS

        self.cf1 = ComplexFormulaOT([self.object_type, self.object_type2], [self.s2, self.s3], LogicalOperator.AND)
        self.cf2 = ComplexFormulaOT([self.object_type, self.object_type2], [self.s1, self.s2], LogicalOperator.OR,
                                    Tense.FUTURE)

    def test_get_states(self):
        self.assertEqual(self.cf1.get_states(), [self.s2, self.s3])
        self.assertEqual(self.cf2.get_states(), [self.s1, self.s2])

    def test_get_model(self):
        self.assertEqual(self.cf1.get_subjects(), [self.object_type, self.object_type2])
        self.assertEqual(self.cf2.get_subjects(), [self.object_type, self.object_type2])

    def test_get_type(self):
        self.assertEqual(self.cf1.get_type(), TypeOfFormula.CF)
        self.assertEqual(self.cf2.get_type(), TypeOfFormula.CF)

    def test_get_complementary_formulas(self):
        self.assertEqual(self.cf1.get_complementary_formulas()[0], ComplexFormulaOT([self.object_type, self.object_type2],
                                                                                  [self.s1, self.s1], LogicalOperator.
                                                                                  AND))
        self.assertEqual(self.cf1.get_complementary_formulas()[2], ComplexFormulaOT([self.object_type, self.object_type2],
                                                                                    [self.s2, self.s1], LogicalOperator.
                                                                                    AND))

    def test_get_tense(self):
        self.assertEqual(self.cf2.get_tense(), Tense.FUTURE)

    def test_eq(self):
        self.assertEqual(self.cf1, self.cf1)
        self.assertNotEqual(self.cf1, self.cf2)