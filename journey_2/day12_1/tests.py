import unittest

from journey_2.day12_1.solution import Solution


class SolutionTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().is_occurences_unique([1,2,2,1,1,3]), True)

    def test_2(self):
        self.assertEqual(Solution().is_occurences_unique([1,2]), False)

    def test_3(self):
        self.assertEqual(Solution().is_occurences_unique([-3,0,1,-3,1,1,1,-3,10,0]), True)
