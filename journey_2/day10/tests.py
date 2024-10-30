import unittest

from journey_2.day10.solution import Solution


class SolutionTest(unittest.TestCase):
    def test_1(self):
        stock_spanner = Solution()

        inputs = [100, 80, 60, 70, 60, 75, 85]
        expected_outputs = [1, 1, 1, 2, 1, 4, 6]

        for i, price in enumerate(inputs):
            with self.subTest(i=i):
                self.assertEqual(stock_spanner.next(price), expected_outputs[i])
