import unittest

from journey_2.day13_2.solution import Solution


class SolutionTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().minimum_cost_stairs([10,15,20]), 15)

    def test_2(self):
        self.assertEqual(Solution().minimum_cost_stairs([1,100,1,1,1,100,1,1,100,1]), 6)
