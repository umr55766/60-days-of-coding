import unittest

from journey_2.day13.solution import Solution


class SolutionTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().get_expiry_minutes([[2,1,1],[1,1,0],[0,1,1]]), 4)

    def test_2(self):
        self.assertEqual(Solution().get_expiry_minutes([[2,1,1],[0,1,1],[1,0,1]]), -1)

    def test_3(self):
        self.assertEqual(Solution().get_expiry_minutes([[0,2]]), 0)
