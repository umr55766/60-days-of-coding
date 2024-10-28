import unittest

from journey_2.day8.solution import Solution


class SolutionTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().unique_paths(3, 7), 28)

    def test_2(self):
        self.assertEqual(Solution().unique_paths(3, 2), 3)
