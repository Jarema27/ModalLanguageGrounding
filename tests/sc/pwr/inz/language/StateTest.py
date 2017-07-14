import unittest
from src.sc.pwr.inz.language.State import State

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.s1 = State.IS
        self.s2 = State.IS_NOT
        self.s3 = State.MAYHAPS

    def test_andS(self):
        s1 = self.s1
        s2 = self.s2
        s3 = self.s3
        self.assertEqual(State.andS(s1, s2), State.MAYHAPS)
        self.assertEqual(State.andS(s1, s3), State.MAYHAPS)
        self.assertEqual(State.andS(s1, s1), State.IS)
        self.assertEqual(State.andS(s2, s2), State.IS_NOT)
        self.assertEqual(State.andS(s3, s3), State.MAYHAPS)
        self.assertEqual(State.andS(s2, s3), State.MAYHAPS)
        self.assertEqual(State.andS(s3, s2), State.MAYHAPS)
        self.assertEqual(State.andS(s1, s3), State.MAYHAPS)
        self.assertEqual(State.andS(s2, s1), State.MAYHAPS)

    def test_orS(self):
        s1 = self.s1
        s2 = self.s2
        s3 = self.s3
        self.assertEqual(State.orS(s1,s2), State.MAYHAPS)
        self.assertEqual(State.orS(s1,s3), State.IS)
        self.assertEqual(State.orS(s1,s1), State.IS)
        self.assertEqual(State.orS(s2,s2), State.IS_NOT)
        self.assertEqual(State.orS(s3,s3), State.MAYHAPS)
        self.assertEqual(State.orS(s2,s3), State.IS_NOT)
        self.assertEqual(State.orS(s3,s2), State.IS_NOT)
        self.assertEqual(State.orS(s1,s3), State.IS)
        self.assertEqual(State.orS(s2,s1), State.MAYHAPS)

    def test_not(self):
        self.assertEqual(State.notS(self.s1), State.IS_NOT)
        self.assertEqual(State.notS(self.s2), State.IS)
        self.assertEqual(State.notS(self.s3), State.MAYHAPS)

    def tearDown(self):
        self.s1 = None
        self.s2 = None
        self.s3 = None

    def test_string(self):
        self.assertEqual(str(self.s1), " is ")
        self.assertEqual(str(self.s2), " is not ")
        self.assertEqual(str(self.s3), " might be ")

if __name__ == '__main__':
    unittest.main()
