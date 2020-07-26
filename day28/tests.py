import unittest

from day28.solution import KSmallestSumPairs


class KSmallestSumPairsTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual([[1, 2], [1, 4], [1, 6]], KSmallestSumPairs([1, 7, 11], [2, 4, 6]).get(3))

    def test_2(self):
        self.assertEqual([[1, 1], [1, 1]], KSmallestSumPairs([1, 1, 2], [1, 2, 3]).get(2))

    def test_3(self):
        self.assertEqual([[1, 3], [2, 3]], KSmallestSumPairs([1, 2], [3]).get(3))
