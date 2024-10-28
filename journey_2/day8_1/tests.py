import unittest

from journey_2.day8_1.solution import Solution


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        self.assertEqual(self.solution.num_of_islands(grid), 1)

    def test_example_2(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        self.assertEqual(self.solution.num_of_islands(grid), 3)

    def test_empty_grid(self):
        grid = []
        self.assertEqual(self.solution.num_of_islands(grid), 0)

    def test_no_islands(self):
        grid = [
            ["0", "0", "0"],
            ["0", "0", "0"],
            ["0", "0", "0"]
        ]
        self.assertEqual(self.solution.num_of_islands(grid), 0)

    def test_multiple_islands(self):
        grid = [
            ["1", "0", "0", "1"],
            ["0", "0", "1", "0"],
            ["1", "0", "0", "1"]
        ]
        self.assertEqual(self.solution.num_of_islands(grid), 5)
