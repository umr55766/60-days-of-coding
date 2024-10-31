import unittest

from journey_2.day11_1.solution import Solution


class SolutionTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().max_vowels("abciiidef", 3), 3)

    def test_2(self):
        self.assertEqual(Solution().max_vowels("aeiou", 2), 2)

    def test_3(self):
        self.assertEqual(Solution().max_vowels("leetcode", 3), 2)
