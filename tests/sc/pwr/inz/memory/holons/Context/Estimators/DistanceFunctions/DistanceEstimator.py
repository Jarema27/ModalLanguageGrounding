import unittest

from src.sc.pwr.inz.memory.holons.Context.Estimators.EstimateFunctions import EstimatorKind
from src.sc.pwr.inz.memory.holons.Context.Estimators.DistanceFunctions.DistanceEstimator import DistanceEstimator
from src.sc.pwr.inz.language.components.State import State

from src.sc.pwr.inz.language.components.Trait import Trait
from src.sc.pwr.inz.memory.episodic.BaseProfile import BaseProfile
from src.sc.pwr.inz.memory.episodic.Observations import Observation
from src.sc.pwr.inz.memory.semantic.IndividualModel import IndividualModel
from src.sc.pwr.inz.memory.semantic.ObjectType import ObjectType
from src.sc.pwr.inz.memory.semantic.identifiers.QRCode import QRCode


class DistanceEstimatorTest(unittest.TestCase):

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
        self.bp4 = BaseProfile(3, [self.o1])
        self.bp6 = BaseProfile(4, [self.o6])

        self.trait_pair = ([self.traits2[2], self.traits[1]], [self.traits2[0], self.traits[1]])

    def test_get_kind_of_estimator(self):
        self.assertEqual(DistanceEstimator.get_kind_of_estimator(), EstimatorKind.DF)

    def test_get_estimated_value(self):
        self.assertEqual(DistanceEstimator.get_estimated_value(self.bp1, self.trait_pair), 3)
        self.assertEqual(DistanceEstimator.get_estimated_value(self.bp2, self.trait_pair), 3)
        self.assertEqual(DistanceEstimator.get_estimated_value(self.bp3, self.trait_pair), 3)
        self.assertEqual(DistanceEstimator.get_estimated_value(self.bp4, self.trait_pair), 2)
        self.assertEqual(DistanceEstimator.get_estimated_value(self.bp6, self.trait_pair), 2)

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
        self.trait_pair = None
