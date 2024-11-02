import unittest

from journey_2.day12.solution import Solution


class SolutionTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().get_pivot_point([1,7,3,6,5,6]   ), 3)

    def test_2(self):
        self.assertEqual(Solution().get_pivot_point([1,2,3]), -1)

    def test_3(self):
        self.assertEqual(Solution().get_pivot_point([2,1,-1]), 0)
