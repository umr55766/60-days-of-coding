import unittest

from journey_1.day30.solution import jumpingOnClouds, repeatedString, minimumBribes, minimumSwaps, arrayManipulation


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(4, jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))

    def test_2(self):
        self.assertEqual(3, jumpingOnClouds([0, 0, 0, 0, 1, 0]))

    def test_3(self):
        self.assertEqual(7, repeatedString("aba", 10))

    def test_4(self):
        self.assertEqual(1000000000000, repeatedString("a", 1000000000000))

    def test_5(self):
        self.assertEqual(3, minimumBribes([2, 1, 5, 3, 4]))

    def test_6(self):
        self.assertEqual("Too chaotic", minimumBribes([2, 5, 1, 3, 4]))

    def test_7(self):
        self.assertEqual(3, minimumSwaps([4, 3, 1, 2]))

    def test_8(self):
        self.assertEqual(3, minimumSwaps([2, 3, 4, 1, 5]))

    def test_9(self):
        self.assertEqual(3, minimumSwaps([1, 3, 5, 2, 4, 6, 7]))

    def test_10(self):
        self.assertEqual(31, arrayManipulation(10, [[2, 6, 8],
                                                 [3, 5, 7],
                                                 [1, 8, 1],
                                                 [5, 9, 15]]))
