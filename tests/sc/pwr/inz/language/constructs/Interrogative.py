import unittest

from src.sc.pwr.inz.language.components.SimpleFormula import SimpleFormula
from src.sc.pwr.inz.memory.holons.BinaryHolon import BinaryHolon
from src.sc.pwr.inz.memory.WokeMemory import WokeMemory
from src.sc.pwr.inz.language.components.ComplexFormula import ComplexFormula
from src.sc.pwr.inz.language.components.LogicalOperator import LogicalOperator
from src.sc.pwr.inz.language.components.State import State

from src.sc.pwr.inz.language.components.Trait import Trait
from src.sc.pwr.inz.memory.episodic.BaseProfile import BaseProfile
from src.sc.pwr.inz.memory.episodic.DistributedKnowledge import DistributedKnowledge
from src.sc.pwr.inz.memory.episodic.Observations import Observation
from src.sc.pwr.inz.memory.holons.NonBinaryHolon import NonBinaryHolon
from src.sc.pwr.inz.memory.semantic.IndividualModel import IndividualModel
from src.sc.pwr.inz.memory.semantic.ObjectType import ObjectType
from src.sc.pwr.inz.memory.semantic.identifiers.QRCode import QRCode
from src.sc.pwr.inz.language.constructs.Interrogative import Interrogative
from src.sc.pwr.inz.language.constructs.Sentence import SentenceType
from src.sc.pwr.inz.language.components.ModalOperator import ModalOperator

class TestInterrogative(unittest.TestCase):

    def setUp(self):

        self.ident1 = QRCode("1")
        self.ident2 = QRCode("2")
        self.ident3 = QRCode("-231")

        self.traits = [Trait("Obly"),Trait("Krasny"), Trait("Sowiecki")]
        self.object_type = ObjectType(1, self.traits)
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
        self.sf1 = SimpleFormula(self.im1, self.traits[1], self.s1)
        self.sf3 = SimpleFormula(self.im2, self.traits2[2], self.s2)

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
        self.dk3 = DistributedKnowledge(self.sf1, [self.bp4])
        self.dk4 = DistributedKnowledge(self.sf3, [self.bp3], 12)
        self.dk5 = DistributedKnowledge(self.cf3, [self.bp1, self.bp4], 1)
        self.dk6 = DistributedKnowledge(self.cf4, [self.bp4, self.bp5, self.bp6, self.bp7], 2)

        self.nbholon1 = NonBinaryHolon(self.dk1)
        self.nbholon2 = NonBinaryHolon(self.dk2)
        self.nbholon3 = NonBinaryHolon(self.dk5)
        self.nbholon4 = NonBinaryHolon(self.dk6)

        self.bholon1 = BinaryHolon(self.dk4)
        self.bholon2 = BinaryHolon(self.dk3)

        self.wM1 = WokeMemory([self.nbholon1, self.nbholon2], [self.bp4, self.bp5, self.bp6, self.bp7])
        self.wM2 = WokeMemory([self.bholon1, self.bholon2], [self.bp4, self.bp5, self.bp6, self.bp7])

        self.interr = Interrogative(self.im1, [self.traits[1]], [State.IS], self.wM2)
        self.interr2 = Interrogative(self.im2, [self.traits2[1], self.traits2[2]], [State.IS, State.IS_NOT],
                                     LogicalOperator.AND, self.wM1)

    def test_get_kind(self):
        self.assertEqual(self.interr.get_kind(), SentenceType.Int)
        self.assertEqual(self.interr2.get_kind(), SentenceType.Int)

    def test_get_subject(self):
        self.assertEqual(self.interr.get_subject(), self.im1)
        self.assertEqual(self.interr2.get_subject(), self.im2)

    def test___str__(self):
        self.assertEqual(str(self.interr), " is  IndividualModel{identifier=QRCode{id=1}} Krasny?")
        self.assertEqual(str(self.interr2), " is  IndividualModel{identifier=QRCode{id=2}}"
                                            " Konieczny and  is not Bolszoj?")

    def test_check_epistemic_scope(self):
        self.assertEqual(Interrogative.check_epistemic_scope([0.15, 0.75, 0.85]),
                         [ModalOperator.NOIDEA, ModalOperator.BEL, ModalOperator.BEL])
        self.assertEqual(Interrogative.check_epistemic_scope([0.15, 0.55, 0.75, 0.95]),
                         [ModalOperator.NOIDEA, ModalOperator.POS,  ModalOperator.BEL, ModalOperator.KNOW])

    def test_get_epistemic_conclusion(self):
        self.assertEqual(self.interr.get_epistemic_conclusion(self.bholon1), [ModalOperator.NOIDEA, ModalOperator.KNOW])
        self.assertEqual(self.interr.get_epistemic_conclusion(self.nbholon4), [ModalOperator.NOIDEA,
                                                                               ModalOperator.NOIDEA,
                                                                               ModalOperator.NOIDEA,
                                                                               ModalOperator.NOIDEA])

    def tearDown(self):
        self.interr = None
        self.interr2 = None
