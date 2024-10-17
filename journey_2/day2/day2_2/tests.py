import unittest

from journey_2.day2.day2_2.solution import Solution


class SolutionTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().method_name([1,12,-5,-6,50,3], 4), 12.75)

    def test_2(self):
        self.assertEqual(Solution().method_name([5], 1), 5.0)

