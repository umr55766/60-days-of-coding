import unittest

from journey_2.day9_1.solution import Solution


class SolutionTest(unittest.TestCase):
    def test_daily_temperatures_case_1(self):
        self.assertEqual(Solution().daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0])

    def test_daily_temperatures_case_2(self):
        self.assertEqual(Solution().daily_temperatures([30, 40, 50, 60]), [1, 1, 1, 0])

    def test_daily_temperatures_case_3(self):
        self.assertEqual(Solution().daily_temperatures([30, 60, 90]), [1, 1, 0])
