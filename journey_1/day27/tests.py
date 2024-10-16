import unittest

from journey_1.day26.solution import BreakDown


class BreakDownTest(unittest.TestCase):
    def test_1(self):
        self.assertTrue(BreakDown("leetcode", ["leet", "code"]).is_breakable())

    def test_2(self):
        self.assertTrue(BreakDown("applepenapple", ["apple", "pen"]).is_breakable())

    def test_3(self):
        self.assertFalse(BreakDown("catsandog", ["cats", "dog", "sand", "and", "cat"]).is_breakable())
