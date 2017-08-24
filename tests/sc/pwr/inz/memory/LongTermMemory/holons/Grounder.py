import unittest

from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.Tense import Tense
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.ComplexFormulaOT import ComplexFormulaOT
from src.sc.pwr.inz.memory.LongTermMemory.semantic.IdentifyingMetaCognition.IndividualModel import IndividualModel
from src.sc.pwr.inz.memory.LongTermMemory.semantic.IdentifyingMetaCognition.ObjectType import ObjectType
from src.sc.pwr.inz.memory.LongTermMemory.holons.Grounder import Grounder
from src.sc.pwr.inz.memory.LongTermMemory.semantic.identifiers.QRCode import QRCode
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.ComplexFormula import ComplexFormula
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.LogicalOperator import LogicalOperator
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.SimpleFormula import SimpleFormula
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.State import State
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.Trait import Trait
from src.sc.pwr.inz.memory.SensoryBufferMemory.Observation import Observation
from src.sc.pwr.inz.memory.ShortTermMemory.episodic.BaseProfile import BaseProfile
from src.sc.pwr.inz.memory.ShortTermMemory.episodic.DistributedKnowledge import DistributedKnowledge


class GrounderTest(unittest.TestCase):

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
        self.o7 = Observation(self.ident1, [(self.traits[0], self.s2), (self.traits[1], self.s1), (self.traits[2],
                                                                                                   self.s1)], 1)
        self.o8 = Observation(self.ident2, [(self.traits2[0], self.s1), (self.traits2[1], self.s2), (self.traits2[2],
                                                                                                     self.s1)], 1)
        self.o9 = Observation(self.ident2, [(self.traits2[0], self.s1), (self.traits2[1], self.s2), (self.traits2[2],
                                                                                                     self.s1)], 1)

        self.bp1 = BaseProfile(1, [self.o1, self.o2, self.o3])
        self.bp2 = BaseProfile(2, [self.o1, self.o5, self.o4])
        self.bp3 = BaseProfile(3, [self.o5, self.o1, self.o3])
        self.bp4 = BaseProfile(3, [self.o5])
        self.bp5 = BaseProfile(14, [self.o7])
        self.bp6 = BaseProfile(4, [self.o6])
        self.bp7 = BaseProfile(324, [self.o8])
        self.bp8 = BaseProfile(34, [self.o9])

        self.cf1 = ComplexFormula(self.im1, [self.traits[0], self.traits[1]], [self.s2, self.s1], LogicalOperator.AND)
        self.cf2 = ComplexFormula(self.im2, [self.traits2[0], self.traits2[1]], [self.s1, self.s1], LogicalOperator.AND)

        self.cf3 = ComplexFormula(self.im2, [self.traits2[0], self.traits2[1]], [self.s1, self.s1], LogicalOperator.OR)

        self.cf4 = ComplexFormula(self.im2, [self.traits2[0], self.traits2[1]], [self.s1, self.s1], LogicalOperator.XOR)

        self.sf1 = SimpleFormula(self.im1, self.traits[1], self.s1)
        self.sf3 = SimpleFormula(self.im2, self.traits2[2], self.s2)
        self.sf4 = SimpleFormula(self.im2, self.traits2[1], self.s1)

        self.dk1 = DistributedKnowledge(self.cf1, [self.bp1, self.bp4], 1)
        self.dk2 = DistributedKnowledge(self.cf2, [self.bp2, self.bp3], 2)

        self.dk3 = DistributedKnowledge(self.sf1, [self.bp4])
        self.dk4 = DistributedKnowledge(self.sf3, [self.bp3], 12)

        self.dk5 = DistributedKnowledge(self.sf4, [self.bp6, self.bp4], 12)

        self.dk6 = DistributedKnowledge(self.cf1, [self.bp5], 12)

        self.dk7 = DistributedKnowledge(self.cf3, [self.bp7], 121)

        self.dk8 = DistributedKnowledge(self.cf4, [self.bp8], 11)

        self.cfot1 = ComplexFormulaOT([self.ident1, self.ident2], [self.s2, self.s1], LogicalOperator.AND)
        self.cfot2 = ComplexFormulaOT([self.ident1, self.ident3], [self.s1, self.s2], LogicalOperator.OR,
                                      Tense.FUTURE)
        self.dk9 = DistributedKnowledge(self.cfot1, [self.bp4], 11)
        self.dk10 = DistributedKnowledge(self.cfot2, [self.bp3, self.bp2], 1321)

    def test_determine_fulfilment(self):
        self.assertEqual(Grounder.determine_fulfilment(self.dk3, self.sf1), 0)
        self.assertEqual(Grounder.determine_fulfilment(self.dk5, self.sf4), 2)

    def test_determine_fulfilment_and(self):
        self.assertEqual(Grounder.determine_fulfilment_cf(self.dk6, self.cf1), 1)
        self.assertEqual(Grounder.determine_fulfilment_cf(self.dk2, self.cf2), 0)

    def test_determine_fulfilment_or(self):
        self.assertEqual(Grounder.determine_fulfilment_cf(self.dk1, self.cf1), 0)
        self.assertEqual(Grounder.determine_fulfilment_cf(self.dk7, self.cf3), 1)

    def test_determine_fulfilment_xor(self):
        self.assertEqual(Grounder.determine_fulfilment_cf(self.dk1, self.cf1), 0)
        self.assertEqual(Grounder.determine_fulfilment_cf(self.dk8, self.cf4), 1)

    def test_determine_fulfilment_ident(self):
        self.assertEqual(Grounder.determine_fulfilment_ident(self.dk9, self.cfot1), 0)
        self.assertEqual(Grounder.determine_fulfilment_ident(self.dk10, self.cfot2), 0)

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
