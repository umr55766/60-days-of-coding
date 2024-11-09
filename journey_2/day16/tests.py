import unittest

from journey_2.day16.solution import Solution


class SolutionTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().is_close("abc", "abbccc"), True)

    def test_2(self):
        self.assertEqual(Solution().is_close("a", "abbccc"), False)

    def test_3(self):
        self.assertEqual(Solution().is_close("cabbba", "abbccc"), True)
