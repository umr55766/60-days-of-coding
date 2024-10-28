import unittest

from journey_2.day8_2.solution import Solution


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        self.assertEqual(self.solution.count_bits(2), [0, 1, 1])

    def test_case_2(self):
        self.assertEqual(self.solution.count_bits(5), [0, 1, 1, 2, 1, 2])

    def test_case_0(self):
        self.assertEqual(self.solution.count_bits(0), [0])

    def test_case_3(self):
        self.assertEqual(self.solution.count_bits(3), [0, 1, 1, 2])

    def test_case_4(self):
        self.assertEqual(self.solution.count_bits(6), [0, 1, 1, 2, 1, 2, 2])
