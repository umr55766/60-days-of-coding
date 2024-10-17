import unittest

from journey_2.day0.solution import ClassName, Solution
from journey_2.day1.solution import MergeStringAlternatively


class SolutionTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().method_name(1), 1)

    def test_2(self):
        self.assertEqual(Solution().method_name(2), 2)

    def test_3(self):
        self.assertEqual(Solution().method_name(3), 3)
