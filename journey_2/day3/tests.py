import unittest

from journey_2.day3.solution import Solution


class SolutionTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().largestAltitude([-5,1,5,0,-7]), 1)

    def test_2(self):
        self.assertEqual(Solution().largestAltitude([-4,-3,-2,-1,4,3,2]), 0)
