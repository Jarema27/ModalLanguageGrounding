import unittest

from src.sc.pwr.inz.memory.LongTermMemory.semantic.IdentifyingMetaCognition.IndividualModel import IndividualModel
from src.sc.pwr.inz.memory.LongTermMemory.semantic.IdentifyingMetaCognition.ObjectType import ObjectType
from src.sc.pwr.inz.memory.LongTermMemory.semantic.identifiers.QRCode import QRCode
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.ComplexFormula import ComplexFormula
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.LogicalOperator import LogicalOperator
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.SimpleFormula import SimpleFormula
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.State import State
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.Trait import Trait
from src.sc.pwr.inz.memory.SensoryBufferMemory.Observation import Observation
from src.sc.pwr.inz.memory.ShortTermMemory.episodic.BaseProfile import BaseProfile
from src.sc.pwr.inz.memory.ShortTermMemory.episodic.DistributedKnowledge import DistributedKnowledge


class TestDistributedKnowledge(unittest.TestCase):

    def setUp(self):
        self.ident1 = QRCode("1")
        self.ident2 = QRCode("2")
        self.ident3 = QRCode("-231")

        self.traits = [Trait("Obly"),Trait("Krasny"), Trait("Sowiecki")]
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
        self.o2 = Observation(self.ident2, [(self.traits[1], self.s3), (self.traits2[1], self.s2), (self.traits[1],
                                                                                                    self.s2)], 1)
        self.o3 = Observation(self.ident3, [(self.traits[2], self.s1), (self.traits2[0], self.s3), (self.traits[2],
                                                                                                    self.s1)])
        self.o4 = Observation(self.ident1, [(self.traits[2], self.s3), (self.traits2[0], self.s3), (self.traits[2],
                                                                                                    self.s2)])
        self.o5 = Observation(self.ident2, [(self.traits[1], self.s1), (self.traits2[1], self.s2), (self.traits[1],
                                                                                                    self.s3)], 1)
        self.bp1 = BaseProfile(1, [self.o1, self.o2, self.o3])
        self.bp2 = BaseProfile(2, [self.o1, self.o5, self.o4])
        self.bp3 = BaseProfile(3, [self.o5, self.o1, self.o3])
        self.bp4 = BaseProfile(3, [self.o5])

        self.cf1 = ComplexFormula(self.im1, [self.traits[0], self.traits[1]], [self.s2, self.s3], LogicalOperator.AND)
        self.cf2 = ComplexFormula(self.im2, [self.traits2[0], self.traits2[1]], [self.s1, self.s1], LogicalOperator.AND)

        self.sf1 = SimpleFormula(self.im1, self.traits[1], self.s1)
        self.sf3 = SimpleFormula(self.im2, self.traits2[2], self.s2)

        self.dk1 = DistributedKnowledge(self.cf1, [self.bp1, self.bp4], 1)
        self.dk2 = DistributedKnowledge(self.cf2, [self.bp2, self.bp3], 2)

        self.dk3 = DistributedKnowledge(self.sf1, [self.bp1, self.bp2])
        self.dk4 = DistributedKnowledge(self.sf3, [self.bp3], 12)

    def test_get_formula(self):
        self.assertEqual(self.dk1.get_formula(), self.cf1)
        self.assertEqual(self.dk2.get_formula(), self.cf2)
        self.assertEqual(self.dk3.get_formula(), self.sf1)

    def test_get_timestamp(self):
        self.assertEqual(self.dk1.get_timestamp(), 1)
        self.assertEqual(self.dk2.get_timestamp(), 2)
        self.assertEqual(self.dk4.get_timestamp(), 12)

    def test_get_bpset(self):
        self.assertEqual(self.dk1.get_bpset(), [self.bp1, self.bp4])
        self.assertEqual(self.dk2.get_bpset(), [self.bp2, self.bp3])
        self.assertEqual(self.dk4.get_bpset(), [self.bp3])

    def test_get_complementary_formulas(self):
        self.assertEqual(self.dk1.get_complementary_formulas(), [
                         ComplexFormula(self.im1,[self.traits[0], self.traits[1]], [self.s1, self.s1], LogicalOperator.AND),
                         ComplexFormula(self.im1, [self.traits[0], self.traits[1]], [self.s1, self.s2], LogicalOperator.AND),
                         ComplexFormula(self.im1, [self.traits[0], self.traits[1]], [self.s2, self.s1], LogicalOperator.AND),
                         ComplexFormula(self.im1, [self.traits[0], self.traits[1]], [self.s2, self.s2], LogicalOperator.AND)])
        self.assertEqual(self.dk3.get_complementary_formulas(), [self.sf1, SimpleFormula(self.im1, self.traits[1],
                                                                                         self.s2)])

    def test_get_grounding_sets(self):
        self.assertEqual(len(self.dk4.get_grounding_sets()), 1)
        self.assertEqual(list(self.dk4.get_grounding_sets().keys())[0], self.sf3.get_traits()[0])
        self.assertEqual(self.dk4.get_grounding_sets(), {self.traits2[2]: self.bp3})

    def test_get_grounding_set(self):
        self.assertEqual(len(self.dk4.get_grounding_set(self.sf1)), 0)
        self.assertEqual(len(self.dk4.get_grounding_set(self.sf3)), 0)
        self.assertEqual(len(self.dk4.get_grounding_set(self.cf1)), 0)

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
