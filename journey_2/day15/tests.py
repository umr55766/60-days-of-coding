import unittest

from journey_2.day15.solution import Solution


class SolutionTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().predict_victory_party("RD"), "Radiant")

    def test_2(self):
        self.assertEqual(Solution().predict_victory_party("RDD"), "Dire")
