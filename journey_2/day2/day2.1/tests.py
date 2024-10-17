import unittest

from journey_2.day2.day3.solution import Solution


class Test(unittest.TestCase):
    def test_1(self):
        array = [0,1,0,3,12]
        Solution().moveZeroes(array)
        self.assertEqual(array, [1,3,12,0,0])

    def test_2(self):
        array = [0]
        Solution().moveZeroes(array)
        self.assertEqual(array, [0])
