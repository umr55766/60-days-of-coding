import unittest

from journey_2.day14.solution import Solution


class SolutionTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().reverse_vowels("IceCreAm"), "AceCreIm")

    def test_2(self):
        self.assertEqual(Solution().reverse_vowels("leetcode"), "leotcede")
