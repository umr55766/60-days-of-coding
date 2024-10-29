import unittest

from journey_2.day9.solution import Solution


class SolutionTest(unittest.TestCase):
    def test_example_1(self):
        intervals = [[1,2],[2,3],[3,4],[1,3]]
        self.assertEqual(Solution().eraseOverlapIntervals(intervals), 1)

    def test_example_2(self):
        intervals = [[1,2],[1,2],[1,2]]
        self.assertEqual(Solution().eraseOverlapIntervals(intervals), 2)

    def test_example_3(self):
        intervals = [[1,2],[2,3]]
        self.assertEqual(Solution().eraseOverlapIntervals(intervals), 0)

    def test_no_intervals(self):
        intervals = []
        self.assertEqual(Solution().eraseOverlapIntervals(intervals), 0)

    def test_single_interval(self):
        intervals = [[1, 2]]
        self.assertEqual(Solution().eraseOverlapIntervals(intervals), 0)

    def test_all_overlapping_intervals(self):
        intervals = [[1,10], [2,3], [3,5], [4,6], [5,7]]
        self.assertEqual(Solution().eraseOverlapIntervals(intervals), 3)