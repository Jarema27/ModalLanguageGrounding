import unittest

from src.sc.pwr.inz.language.Grounder import Grounder
from src.sc.pwr.inz.memory.semantic.ObjectType import ObjectType
from src.sc.pwr.inz.memory.semantic.IndividualModel import IndividualModel
from src.sc.pwr.inz.memory.episodic.DistributedKnowledge import DistributedKnowledge
from src.sc.pwr.inz.language.SimpleFormula import SimpleFormula
from src.sc.pwr.inz.language.ComplexFormula import ComplexFormula
from src.sc.pwr.inz.memory.episodic.BaseProfile import BaseProfile
from src.sc.pwr.inz.language.State import State
from src.sc.pwr.inz.language.Trait import Trait
from src.sc.pwr.inz.memory.episodic.Observations import Observation
from src.sc.pwr.inz.memory.semantic.identifiers.QRCode import QRCode


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
        self.bp1 = BaseProfile(1, [self.o1, self.o2, self.o3])
        self.bp2 = BaseProfile(2, [self.o1, self.o5, self.o4])
        self.bp3 = BaseProfile(3, [self.o5, self.o1, self.o3])
        self.bp4 = BaseProfile(3, [self.o5])
        self.bp6 = BaseProfile(4, [self.o6])

        self.cf1 = ComplexFormula(self.im1, [self.traits[0], self.traits[1]], [self.s2, self.s3])
        self.cf2 = ComplexFormula(self.im2, [self.traits2[0], self.traits2[1]], [self.s1, self.s1])

        self.sf1 = SimpleFormula(self.im1, self.traits[1], self.s1)
        self.sf3 = SimpleFormula(self.im2, self.traits2[2], self.s2)
        self.sf4 = SimpleFormula(self.im2, self.traits2[1], self.s1)

        self.dk1 = DistributedKnowledge(self.cf1, [self.bp1, self.bp4], 1)
        self.dk2 = DistributedKnowledge(self.cf2, [self.bp2, self.bp3], 2)

        self.dk3 = DistributedKnowledge(self.sf1, [self.bp4])
        self.dk4 = DistributedKnowledge(self.sf3, [self.bp3], 12)

        self.dk5 = DistributedKnowledge(self.sf4, [self.bp6,self.bp4], 12)

    def test_determine_fulfilment(self):
        self.assertEqual(Grounder.determine_fulfilment(self.dk3, self.sf1), 0)
        self.assertEqual(Grounder.determine_fulfilment(self.dk5, self.sf4), 2)

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