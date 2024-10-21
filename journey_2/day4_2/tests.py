import unittest

from journey_2.day4_2.solution import Solution


class SolutionTest(unittest.TestCase):
    def test_recent_counter(self):
        recent_counter = Solution()

        self.assertEqual(recent_counter.ping(1), 1)
        self.assertEqual(recent_counter.ping(100), 2)
        self.assertEqual(recent_counter.ping(3001), 3)
        self.assertEqual(recent_counter.ping(3002), 3)
