import unittest

from journey_2.day0.solution import ClassName
from journey_2.day1.solution import MergeStringAlternatively
from journey_2.day2.solution import GCDString


class ClassNameTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(GCDString.calculate(1), 1)

    def test_2(self):
        self.assertEqual(GCDString.calculate(2), 2)

    def test_3(self):
        self.assertEqual(GCDString.calculate(3), 3)
