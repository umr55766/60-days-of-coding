import unittest

from journey_2.day7.solution import Solution


class SolutionTest(unittest.TestCase):
    def test_case_1(self):
        maze = [["+", "+", ".", "+"],
                [".", ".", ".", "+"],
                ["+", "+", "+", "."]]
        entrance = [1, 2]
        expected_output = 1
        self.assertEqual(Solution().nearest_exit(maze, entrance), expected_output)

    def test_case_2(self):
        maze = [["+", "+", "+"],
                [".", ".", "."],
                ["+", "+", "+"]]
        entrance = [1, 0]
        expected_output = 2
        self.assertEqual(Solution().nearest_exit(maze, entrance), expected_output)

    def test_case_3(self):
        maze = [[".", "+"]]
        entrance = [0, 0]
        expected_output = -1
        self.assertEqual(Solution().nearest_exit(maze, entrance), expected_output)


    def test_case_4(self):
        maze = [["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".",".",".","+"],["+","+","+","+",".","+","."]]
        entrance = [0, 1]
        expected_output = 7
        self.assertEqual(Solution().nearest_exit(maze, entrance), expected_output)

