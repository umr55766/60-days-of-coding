import unittest

from journey_2.day11.solution import Solution


class SolutionTest(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(Solution().is_subsequence("abc", "ahbgdc"), True)

    def test_example_2(self):
        self.assertEqual(Solution().is_subsequence("axc", "ahbgdc"), False)
