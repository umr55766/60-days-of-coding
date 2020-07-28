import unittest

from day30.solution import jumpingOnClouds


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(4, jumpingOnClouds([0,0,1,0,0,1,0]))

    def test_2(self):
        self.assertEqual(3, jumpingOnClouds([0,0,0,0,1,0]))
