import unittest

from src.sc.pwr.inz.memory.LongTermMemory.semantic.IdentifyingMetaCognition.Cluster import Cluster
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.Trait import Trait


class ObjectTypeTest(unittest.TestCase):

    def setUp(self):
        self.traits = [Trait("Obly"), Trait("Krasny"), Trait("Sowiecki")]
        self.traits2 = [Trait("Barowalny"), Trait("Konieczny"), Trait("Bolszoj")]
        self.cl1 = Cluster("Płaz", self.traits)

    def test_check_name(self):
        self.assertEqual(self.cl1.get_string(), "Płaz")

    def test_get_traits(self):
        self.assertEqual(self.cl1.get_traits(),self.traits)
