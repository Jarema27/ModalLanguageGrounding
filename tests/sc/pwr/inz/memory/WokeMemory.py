import unittest

from src.sc.pwr.inz.memory.LongTermMemory.WokeMemory import WokeMemory
from src.sc.pwr.inz.memory.LongTermMemory.holons.NonBinaryHolon import NonBinaryHolon
from src.sc.pwr.inz.memory.LongTermMemory.semantic.IdentifyingMetaCognition.IndividualModel import IndividualModel
from src.sc.pwr.inz.memory.LongTermMemory.semantic.IdentifyingMetaCognition.ObjectType import ObjectType
from src.sc.pwr.inz.memory.LongTermMemory.semantic.identifiers.QRCode import QRCode
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.ComplexFormula import ComplexFormula
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.LogicalOperator import LogicalOperator
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.State import State
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.Trait import Trait
from src.sc.pwr.inz.memory.SensoryBufferMemory.Observation import Observation
from src.sc.pwr.inz.memory.ShortTermMemory.episodic.BaseProfile import BaseProfile
from src.sc.pwr.inz.memory.ShortTermMemory.episodic.DistributedKnowledge import DistributedKnowledge


class TestWokeMemory(unittest.TestCase):

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

        self.nbholon1 = NonBinaryHolon(self.dk1)
        self.nbholon2 = NonBinaryHolon(self.dk2)
        self.nbholon3 = NonBinaryHolon(self.dk5)
        self.nbholon4 = NonBinaryHolon(self.dk6)

        self.wM1 = WokeMemory([self.nbholon1, self.nbholon2], [self.bp4, self.bp5, self.bp6, self.bp7])

    def test_get_holons(self):
        self.assertEqual(self.wM1.get_holons(), [self.nbholon1, self.nbholon2])
        self.assertNotEqual(self.wM1.get_holons(), [self.nbholon1, self.nbholon3])

    def test_add_bp(self):
        self.wM1.add_bp(self.bp1)
        self.assertEqual(self.wM1.get_bpcollective(), [self.bp4, self.bp5, self.bp6, self.bp7, self.bp1])

    def test_get_distributed_knowledge(self):
        dk = self.wM1.get_distributed_knowledge(self.cf4, 20, 0)
        self.assertEqual(dk, DistributedKnowledge(self.cf4, [self.bp4, self.bp5, self.bp6, self.bp7],
                                                  dk.get_timestamp()))

    def test_get_holon_by_formula(self):
        self.assertEqual(self.wM1.get_holon_by_formula(self.cf2, 1), self.nbholon2)

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
        self.nbholon2 = None
        self.nbholon1 = None
