import unittest

from journey_2.day2.solution import GCDString


class ClassNameTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(GCDString.calculate("ABCABC", "ABC"), "ABC")

    def test_2(self):
        self.assertEqual(GCDString.calculate("ABABAB", "ABAB"), "AB")

    def test_3(self):
        self.assertEqual(GCDString.calculate("LEET", "CODE"), "")
