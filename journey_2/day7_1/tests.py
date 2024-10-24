import unittest

from journey_2.day7_1.solution import Solution


class SolutionTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().find_kth_largest([3,2,1,5,6,4], 2), 5)

    def test_2(self):
        self.assertEqual(Solution().find_kth_largest([3,2,3,1,2,4,5,5,6], 4), 4)