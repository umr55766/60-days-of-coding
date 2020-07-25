import unittest

from day27.solution import DuplicateDetector


class BreakDownTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(2, DuplicateDetector([1,3,4,2,2]).detect())

    def test_2(self):
        self.assertEqual(3, DuplicateDetector([3,1,3,4,2]).detect())
