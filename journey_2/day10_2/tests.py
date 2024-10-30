import unittest

from journey_2.day10_2.solution import Solution


class SolutionTest(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(Solution().combination_sum(3, 7), [[1, 2, 4]])

    def test_example_2(self):
        self.assertEqual(Solution().combination_sum(3, 9), [[1, 2, 6], [1, 3, 5], [2, 3, 4]])

    def test_example_3(self):
        self.assertEqual(Solution().combination_sum(4, 1), [])

    def test_example_4(self):
        self.assertEqual(Solution().combination_sum(2, 5), [[1, 4], [2, 3]])
