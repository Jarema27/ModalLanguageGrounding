import unittest
from src.sc.pwr.inz.memory.semantic.identifiers.QRCode import QRCode


class IdentifierTestCase(unittest.TestCase):

    def setUp(self):
        self.ident1 = QRCode("1")
        self.ident2 = QRCode("2")
        self.ident3 = QRCode("-231")

    def test_to_str(self):
        self.assertEquals(str(self.ident1), "QRCode{id=1}")

    def tearDown(self):
        self.ident1 = None
        self.ident2 = None
        self.ident3 = None
