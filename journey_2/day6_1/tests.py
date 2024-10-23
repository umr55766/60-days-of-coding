import unittest

from journey_2.day6_1.solution import Solution


class SolutionTest(unittest.TestCase):
    def test_1(self):
        rooms = [[1], [2], [3], []]
        result = Solution().can_visit_all_rooms(rooms)
        self.assertEqual(result, True)

    def test_2(self):
        rooms = [[1, 3], [3, 0, 1], [2], [0]]
        result = Solution().can_visit_all_rooms(rooms)
        self.assertEqual(result, False)
