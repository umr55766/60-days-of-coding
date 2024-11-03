import unittest

from journey_2.day13_1.solution import Solution


class SolutionTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().get_longest_subsequence_length("abcde", "ace"), 3)

    def test_2(self):
        self.assertEqual(Solution().get_longest_subsequence_length("abc", "abc"), 3)

    def test_3(self):
        self.assertEqual(Solution().get_longest_subsequence_length("abc", "def"), 0)

    def test_4(self):
        self.assertEqual(Solution().get_longest_subsequence_length("abcba", "abcbcba"), 5)
