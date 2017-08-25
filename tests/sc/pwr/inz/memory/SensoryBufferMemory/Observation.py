import unittest

from src.sc.pwr.inz.memory.SensoryBufferMemory.Observation import Observation
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.State import State
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.Trait import Trait
from src.sc.pwr.inz.memory.LongTermMemory.semantic.identifiers.QRCode import QRCode


class ObservationsTest(unittest.TestCase):

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

    def test_str(self):
        print(self.o2)
        self.assertEqual(str(self.o2), "{QRCode{id=2} ['Krasny  might_be ', 'Konieczny  is_not ',"
                                       " 'Krasny  is_not '] observed: 1}")

    def test_get_identifier(self):
        self.assertEqual(self.o1.get_identifier(), self.ident1)
        self.assertEqual(self.o2.get_identifier(), self.ident2)
        self.assertEqual(self.o3.get_identifier(), self.ident3)

    def test_get_observed(self):
        self.assertEqual(self.o1.get_observed(), [(self.traits[0], self.s1), (self.traits2[2], self.s1), (self.traits[1]
                                                                                                          , self.s2)])
        self.assertEqual(self.o2.get_observed(),  [(self.traits[1], self.s3), (self.traits2[1], self.s2), (self.traits[1],
                                                                                                           self.s2)])

    def test_get_timestamp(self):
        self.assertEqual(self.o2.get_episode(), 1)

    def test_eq(self):
        self.assertEqual(self.o1, self.o1)
        self.assertNotEqual(self.o1, self.o2)
        self.assertEqual(self.o2, self.o2)

    def tearDown(self):
        self.traits2 = None
        self.traits = None
        self.ident1 = None
        self.ident2 = None
        self.ident3 = None
        self.o1 = None
        self.o2 = None
        self.o3 = None
        self.s1 = None
        self.s2 = None
        self.s3 = None
