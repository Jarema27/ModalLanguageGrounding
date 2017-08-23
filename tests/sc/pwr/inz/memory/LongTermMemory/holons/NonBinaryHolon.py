import unittest

from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.Tense import Tense
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.ComplexFormulaOT import ComplexFormulaOT
from src.sc.pwr.inz.memory.LongTermMemory.semantic.IdentifyingMetaCognition.IndividualModel import IndividualModel
from src.sc.pwr.inz.memory.LongTermMemory.semantic.IdentifyingMetaCognition.ObjectType import ObjectType
from src.sc.pwr.inz.memory.LongTermMemory.holons.Context.CompositeContext import CompositeContext
from src.sc.pwr.inz.memory.LongTermMemory.holons.Context.Estimators.DistanceFunctions.DistanceEstimator import \
    DistanceEstimator
from src.sc.pwr.inz.memory.LongTermMemory.holons.Holon import HolonKind
from src.sc.pwr.inz.memory.LongTermMemory.holons.NonBinaryHolon import NonBinaryHolon
from src.sc.pwr.inz.memory.LongTermMemory.semantic.identifiers.QRCode import QRCode
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.ComplexFormula import ComplexFormula
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.LogicalOperator import LogicalOperator
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.State import State
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.Trait import Trait
from src.sc.pwr.inz.memory.SensoryBufferMemory.Observation import Observation
from src.sc.pwr.inz.memory.ShortTermMemory.episodic.BaseProfile import BaseProfile
from src.sc.pwr.inz.memory.ShortTermMemory.episodic.DistributedKnowledge import DistributedKnowledge


class TestNonBinaryHolon(unittest.TestCase):
    def setUp(self):
        self.ident1 = QRCode("1")
        self.ident2 = QRCode("2")
        self.ident3 = QRCode("-231")

        self.traits = [Trait("Obly"), Trait("Krasny"), Trait("Sowiecki")]
        self.traits2 = [Trait("Barowalny"), Trait("Konieczny"), Trait("Bolszoj")]

        self.s1 = State.IS
        self.s2 = State.IS_NOT
        self.s3 = State.MAYHAPS

        self.object_type = ObjectType(1, self.traits)
        self.object_type2 = ObjectType(2, self.traits2)

        self.im1 = IndividualModel(self.ident1, self.object_type)
        self.im2 = IndividualModel(self.ident2, self.object_type2)

        self.o1 = Observation(self.ident1, [(self.traits[0], self.s1), (self.traits2[2], self.s1), (self.traits[1],
                                                                                                    self.s2)])
        self.o2 = Observation(self.ident2, [(self.traits[1], self.s1), (self.traits2[1], self.s2), (self.traits[1],
                                                                                                    self.s2)], 1)
        self.o3 = Observation(self.ident3, [(self.traits[2], self.s1), (self.traits2[0], self.s3), (self.traits[2],
                                                                                                    self.s1)])
        self.o4 = Observation(self.ident1, [(self.traits[2], self.s3), (self.traits2[0], self.s3), (self.traits[2],
                                                                                                    self.s2)])
        self.o5 = Observation(self.ident2, [(self.traits2[1], self.s2), (self.traits2[2], self.s2), (self.traits[1],
                                                                                                     self.s3)], 1)

        self.o6 = Observation(self.ident2, [(self.traits2[1], self.s1), (self.traits[1], self.s1), (self.traits2[2],
                                                                                                    self.s1)], 1)
        self.o7 = Observation(self.ident2, [(self.traits2[1], self.s1), (self.traits[1], self.s1), (self.traits2[2],
                                                                                                    self.s1)], 1)
        self.o8 = Observation(self.ident2, [(self.traits2[1], self.s2), (self.traits[1], self.s1), (self.traits2[2],
                                                                                                    self.s1)], 1)
        self.o9 = Observation(self.ident2, [(self.traits2[1], self.s1), (self.traits[1], self.s1), (self.traits2[2],
                                                                                                    self.s2)], 1)

        self.bp1 = BaseProfile(1, [self.o1, self.o2, self.o3])
        self.bp2 = BaseProfile(2, [self.o1, self.o5, self.o4])
        self.bp3 = BaseProfile(3, [self.o5, self.o1, self.o3])
        self.bp4 = BaseProfile(3, [self.o5])
        self.bp5 = BaseProfile(3, [self.o7])
        self.bp6 = BaseProfile(3, [self.o8])
        self.bp7 = BaseProfile(3, [self.o9])

        self.cf1 = ComplexFormula(self.im1, [self.traits[0], self.traits[1]], [self.s2, self.s3], LogicalOperator.AND)
        self.cf2 = ComplexFormula(self.im2, [self.traits2[0], self.traits2[1]], [self.s1, self.s1], LogicalOperator.AND)
        self.cf3 = ComplexFormula(self.im1, [self.traits[1], self.traits[2]], [self.s2, self.s1], LogicalOperator.AND)
        self.cf4 = ComplexFormula(self.im2, [self.traits2[1], self.traits2[2]], [self.s1, self.s1], LogicalOperator.AND)

        self.dk1 = DistributedKnowledge(self.cf1, [self.bp1, self.bp4], 1)
        self.dk2 = DistributedKnowledge(self.cf2, [self.bp2, self.bp3], 2)

        self.dk5 = DistributedKnowledge(self.cf3, [self.bp1, self.bp4], 1)
        self.dk6 = DistributedKnowledge(self.cf4, [self.bp4, self.bp5, self.bp6, self.bp7], 2)

        self.DE = DistanceEstimator()
        self.CC = CompositeContext(self.DE, [self.bp1, self.bp4], 1, 1)
        self.CC2 = CompositeContext(self.DE, [self.bp4, self.bp5, self.bp6, self.bp7], 1, 1)
        self.CC3 = CompositeContext(self.DE, [self.bp4, self.bp5, self.bp6, self.bp7], 3, 1)

        self.nbholon1 = NonBinaryHolon(self.dk1)
        self.nbholon2 = NonBinaryHolon(self.dk2)
        self.nbholon3 = NonBinaryHolon(self.dk5)
        self.nbholon4 = NonBinaryHolon(self.dk6)
        self.nbholon5 = NonBinaryHolon(self.dk5, self.CC.get_contextualized_bpset())
        self.nbholon6 = NonBinaryHolon(self.dk6, self.CC2.get_contextualized_bpset())
        self.nbholon7 = NonBinaryHolon(self.dk6, self.CC3.get_contextualized_bpset())

        self.cfot1 = ComplexFormulaOT([self.ident1, self.ident2], [self.s2, self.s1], LogicalOperator.AND)
        self.cfot2 = ComplexFormulaOT([self.ident1, self.ident3], [self.s1, self.s2], LogicalOperator.OR,
                                      Tense.FUTURE)
        self.dk9 = DistributedKnowledge(self.cfot1, [self.bp4], 11)
        self.dk10 = DistributedKnowledge(self.cfot2, [self.bp3, self.bp2], 1321)
        self.nbholon8 = NonBinaryHolon(self.dk10)

    def test_get_tao(self):
        self.assertEqual(self.nbholon1.get_tao(), [0.0, 0.0, 0.0, 0.0])
        self.assertEqual(self.nbholon2.get_tao(), [0, 0, 0, 0])
        self.assertEqual(self.nbholon3.get_tao(), [0.0, 0.0, 0.0, 0.0])
        self.assertEqual(self.nbholon4.get_tao(), [0.25, 0.25, 0.25, 0.25])
        self.assertEqual(self.nbholon8.get_tao(), [0.3333333333333333,
                                                   0.3333333333333333,
                                                   0.16666666666666666,
                                                   0.16666666666666666])

    def test_get_complementary_formulas(self):
        self.assertEqual(self.nbholon4.get_complementary_formulas(), self.cf4.get_complementary_formulas())

    def test_get_kind(self):
        self.assertEqual(self.nbholon4.get_kind(), HolonKind.NBH)

    def test_is_applicable(self):
        self.assertTrue(self.nbholon4.is_applicable(self.cf4))
        self.assertTrue(self.nbholon4.is_applicable(ComplexFormula(self.im2, [self.traits2[1], self.traits2[2]],
                                                                   [self.s2, self.s2], LogicalOperator.AND)))

    def test_get_formula(self):
        self.assertEqual(self.nbholon4.get_formula(), self.cf4)

    def test_get_tao_for_state(self):
        self.assertEqual(self.nbholon4.get_tao_for_state(self.s1, self.s2), 0.25)

    def test_context(self):
        self.assertEqual(self.nbholon5.get_tao(), [0.0, 0.0, 0.0, 0.0])
        self.assertEqual(self.nbholon6.get_tao(), [0.0, 0.3333333333333333, 0.3333333333333333,
                                                   0.3333333333333333])
        self.assertEqual(self.nbholon7.get_tao(), [0.25, 0.25, 0.25, 0.25])

    def tearDown(self):
        self.traits2 = None
        self.traits = None
        self.ident1 = None
        self.ident2 = None
        self.ident3 = None
        self.o1 = None
        self.o2 = None
        self.o3 = None
        self.o4 = None
        self.o5 = None
        self.s1 = None
        self.s2 = None
        self.s3 = None
        self.bp1 = None
        self.bp2 = None
        self.bp3 = None
