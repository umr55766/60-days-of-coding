import unittest

from journey_2.day10_1.solution import Solution


class SolutionTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().find_min_arrow_shots([[10, 16], [2, 8], [1, 6], [7, 12]]), 2)

    def test_2(self):
        self.assertEqual(Solution().find_min_arrow_shots([[1, 2], [3, 4], [5, 6], [7, 8]]), 4)

    def test_3(self):
        self.assertEqual(Solution().find_min_arrow_shots([[1, 2], [2, 3], [3, 4], [4, 5]]), 2)

