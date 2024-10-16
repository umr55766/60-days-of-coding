import unittest

from journey_2.day1.solution import MergeStringAlternatively


class MergeStringAlternativelyTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(MergeStringAlternatively().merge("abc", "pqr"), "apbqcr")

    def test_2(self):
        self.assertEqual(MergeStringAlternatively().merge("ab", "pqrs"), "apbqrs")

    def test_3(self):
        self.assertEqual(MergeStringAlternatively().merge("abcd", "pq"), "apbqcd")
