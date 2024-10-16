import unittest

from journey_1.day22.solution import PhoneKeypad


class PhoneKeypadTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], PhoneKeypad("23").get_combinations())