import unittest

from src.sc.pwr.inz.memory.LongTermMemory.semantic.IdentifyingMetaCognition.IndividualModel import IndividualModel
from src.sc.pwr.inz.memory.LongTermMemory.semantic.IdentifyingMetaCognition.ObjectType import ObjectType
from src.sc.pwr.inz.memory.LongTermMemory.holons.BinaryHolon import BinaryHolon
from src.sc.pwr.inz.memory.LongTermMemory.holons.Context.CompositeContext import CompositeContext
from src.sc.pwr.inz.memory.LongTermMemory.holons.Context.Estimators.DistanceFunctions.DistanceEstimator import \
    DistanceEstimator
from src.sc.pwr.inz.memory.LongTermMemory.holons.Holon import HolonKind
from src.sc.pwr.inz.memory.LongTermMemory.semantic.identifiers.QRCode import QRCode
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.ComplexFormula import ComplexFormula
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.LogicalOperator import LogicalOperator
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.SimpleFormula import SimpleFormula
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.State import State
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.Trait import Trait
from src.sc.pwr.inz.memory.SensoryBufferMemory.Observation import Observation
from src.sc.pwr.inz.memory.ShortTermMemory.episodic.BaseProfile import BaseProfile
from src.sc.pwr.inz.memory.ShortTermMemory.episodic.DistributedKnowledge import DistributedKnowledge


class BinaryHolonTest(unittest.TestCase):

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
        self.o5 = Observation(self.ident2, [(self.traits[1], self.s1), (self.traits2[1], self.s1), (self.traits[1],
                                                                                                    self.s3)], 1)

        self.o6 = Observation(self.ident2, [(self.traits2[1], self.s1), (self.traits[1], self.s1), (self.traits2[2],
                                                                                                    self.s1)], 1)
        self.o7 = Observation(self.ident2, [(self.traits2[1], self.s2), (self.traits[1], self.s1), (self.traits2[2],
                                                                                                    self.s1)], 1)

        self.bp1 = BaseProfile(1, [self.o1, self.o2, self.o3])
        self.bp2 = BaseProfile(2, [self.o1, self.o5, self.o4])
        self.bp3 = BaseProfile(3, [self.o5, self.o1, self.o3])
        self.bp4 = BaseProfile(3, [self.o5])
        self.bp6 = BaseProfile(4, [self.o6])
        self.bp7 = BaseProfile(4, [self.o7])

        self.cf1 = ComplexFormula(self.im1, [self.traits[0], self.traits[1]], [self.s2, self.s3], LogicalOperator.AND)
        self.cf2 = ComplexFormula(self.im2, [self.traits2[0], self.traits2[1]], [self.s1, self.s1], LogicalOperator.AND)

        self.sf1 = SimpleFormula(self.im1, self.traits[1], self.s1)
        self.sf3 = SimpleFormula(self.im2, self.traits2[2], self.s2)
        self.sf4 = SimpleFormula(self.im2, self.traits2[1], self.s1)
        self.sf5 = SimpleFormula(self.im2, self.traits2[1], self.s2)

        self.dk1 = DistributedKnowledge(self.cf1, [self.bp1, self.bp4], 1)
        self.dk2 = DistributedKnowledge(self.cf2, [self.bp2, self.bp3], 2)

        self.dk3 = DistributedKnowledge(self.sf1, [self.bp4])
        self.dk4 = DistributedKnowledge(self.sf3, [self.bp3], 12)

        self.dk5 = DistributedKnowledge(self.sf4, [self.bp6, self.bp4], 12)
        self.dk6 = DistributedKnowledge(self.sf5, [self.bp6, self.bp7], 12)

        self.DE = DistanceEstimator()
        self.CC = CompositeContext(self.DE, [self.bp6, self.bp7], 1, 1)
        self.CC2 = CompositeContext(self.DE, [self.bp6, self.bp7, self.bp4], 1, 1)
        self.CC3 = CompositeContext(self.DE, [self.bp6, self.bp6, self.bp2], 2, 1)

        self.bholon1 = BinaryHolon(self.dk3)
        self.bholon2 = BinaryHolon(self.dk4)
        self.bholon3 = BinaryHolon(self.dk5)
        self.bholon4 = BinaryHolon(self.dk6)
        self.bholon5 = BinaryHolon(self.dk6, self.CC.get_contextualized_bpset())
        self.bholon6 = BinaryHolon(self.dk3, self.CC2.get_contextualized_bpset())
        self.bholon7 = BinaryHolon(self.dk5, self.CC2.get_contextualized_bpset())
        self.bholon8 = BinaryHolon(self.dk5, self.CC3.get_contextualized_bpset())

    def test_get_tao(self):
        self.assertEqual(self.bholon1.get_tao(), [0, 0])
        self.assertEqual(self.bholon2.get_tao(), [0, 0])
        self.assertEqual(self.bholon3.get_tao(), [1.0, 0])
        self.assertEqual(self.bholon4.get_tao(), [0.5, 0.5])

    def test_get_kind(self):
        self.assertEqual(self.bholon1.get_kind(), HolonKind.BH)

    def test_get_formula(self):
        self.assertEqual(self.bholon1.get_formula(), self.sf1)

    def test_get_complementary_formulas(self):
        self.assertEqual(self.bholon1.get_complementary_formulas(), self.sf1.get_complementary_formulas())

    def test_is_applicable(self):
        self.assertTrue(self.bholon1.is_applicable(self.sf1))
        self.assertFalse(self.bholon1.is_applicable(self.sf5))

    def test_get_tao_for_state(self):
        self.assertEqual(self.bholon1.get_tao_for_state(self.s1), 0.0)

    def test_context(self):
        self.assertEqual(self.bholon5.get_tao(), [0.5, 0.5])
        self.assertEqual(self.bholon7.get_tao(), [0.6666666666666666, 0.3333333333333333])
        self.assertEqual(self.bholon7.get_context(), [self.bp6, self.bp7, self.bp4])
        self.assertEqual(self.bholon6.get_tao(), [0.0, 0.0])
        self.assertEqual(self.bholon8.get_context(), [self.bp6, self.bp6, self.bp2])

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
