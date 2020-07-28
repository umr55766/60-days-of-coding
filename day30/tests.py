import unittest

from day30.solution import jumpingOnClouds, repeatedString


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(4, jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))

    def test_2(self):
        self.assertEqual(3, jumpingOnClouds([0, 0, 0, 0, 1, 0]))

    def test_3(self):
        self.assertEqual(7, repeatedString("aba",10))

    def test_4(self):
        self.assertEqual(1000000000000, repeatedString("a", 1000000000000))
