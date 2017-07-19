import unittest

from src.sc.pwr.inz.memory.episodic.BaseProfile import BaseProfile
from src.sc.pwr.inz.language.State import State
from src.sc.pwr.inz.language.Trait import Trait
from src.sc.pwr.inz.memory.episodic.Observations import Observation
from src.sc.pwr.inz.memory.semantic.identifiers.QRCode import QRCode


class BaseProfileTest(unittest.TestCase):

    def setUp(self):
        self.ident1 = QRCode("1")
        self.ident2 = QRCode("2")
        self.ident3 = QRCode("-231")

        self.traits = [Trait("Obly"),Trait("Krasny"), Trait("Sowiecki")]
        self.traits2 = [Trait("Barowalny"), Trait("Konieczny"), Trait("Bolszoj")]

        self.s1 = State.IS
        self.s2 = State.IS_NOT
        self.s3 = State.MAYHAPS

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

    def test_get_timestamp(self):
        self.assertEqual(self.bp1.get_timestamp(), 1)
        self.assertEqual(self.bp2.get_timestamp(), 2)
        self.assertEqual(self.bp3.get_timestamp(), 3)

    def test_get_observations_is(self):
        self.assertEqual(self.bp4.get_observations_is(), {self.traits[1]: self.o5})
        self.assertEqual(self.bp2.get_observations_is(), {self.traits[0]: self.o1, self.traits2[2]: self.o1,
                                                          self.traits[1]: self.o5})

    def test_get_observations_is_not(self):
        self.assertEqual(self.bp4.get_observations_is_not(), {self.traits2[1]: self.o5})
        self.assertEqual(self.bp2.get_observations_is_not(), {self.traits[1]: self.o1, self.traits2[1]: self.o5,
                                                              self.traits[2]: self.o4})

    def test_get_observations_mayhaps(self):
        self.assertEqual(self.bp4.get_observations_mayhaps(), {self.traits[1]: self.o5})
        self.assertEqual(self.bp3.get_observations_mayhaps(), {self.traits[1]: self.o5, self.traits2[0]: self.o3})

    def test_add_observations_is(self):
        newo = Observation(self.ident2, [(self.traits[1], self.s1)], 1)
        self.bp4.add_observation_is_kind([newo])
        self.assertEqual(self.bp4.get_observations_is(), {self.traits[1]: self.o5, self.traits[1]: newo})

    def test_get_observed_ims(self):
        self.assertEqual(self.bp4.get_observed_ims(), [self.ident2])
        self.assertEqual(len(self.bp2.get_observed_ims()), 2)
        self.assertTrue(self.ident2 in self.bp2.get_observed_ims() and self.ident1 in self.bp2.get_observed_ims())
        self.assertTrue(self.ident1 in self.bp3.get_observed_ims() and self.ident2 in self.bp3.get_observed_ims() and
                        self.ident3 in self.bp3.get_observed_ims())

    def test_check_if_observed(self):
        self.assertTrue(self.bp4.check_if_observed(self.ident2, [(self.traits[1], self.s1), (self.traits2[1], self.s2),
                                                                 (self.traits[1], self.s3)]))

    def test_add_observation_which_state_you_know_not(self):
        newo = Observation(self.ident2, [(self.traits[1], self.s1)], 1)
        self.bp4.add_observation_which_state_you_know_not(newo)
        self.assertEqual(self.bp4.get_observations_is(), {self.traits[1]: self.o5, self.traits[1]: newo})

    def test_give_all_traits_involved(self):
        self.assertEquals(self.bp4.give_all_traits_involved(), [self.traits2[1], self.traits[1]])

    def test_eq(self):

        bp4prim = BaseProfile(3, [self.o5])
        self.assertTrue(self.bp4 == bp4prim)

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
