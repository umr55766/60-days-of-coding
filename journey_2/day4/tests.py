import unittest

from journey_2.day4.solution import Solution

class SolutionTest(unittest.TestCase):
    def test_asteroids_case_1(self):
        asteroids = [5, 10, -5]
        expected_output = [5, 10]
        self.assertEqual(Solution().asteroid_collision(asteroids), expected_output)

    def test_asteroids_case_2(self):
        asteroids = [8, -8]
        expected_output = []
        self.assertEqual(Solution().asteroid_collision(asteroids), expected_output)

    def test_asteroids_case_3(self):
        asteroids = [10, 2, -5]
        expected_output = [10]
        self.assertEqual(Solution().asteroid_collision(asteroids), expected_output)

    def test_asteroids_case_4(self):
        asteroids = [-2, -1, 1, 2]
        expected_output = [-2, -1, 1, 2]
        self.assertEqual(Solution().asteroid_collision(asteroids), expected_output)
