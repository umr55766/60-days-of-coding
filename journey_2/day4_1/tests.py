import unittest

from journey_2.day4_1.solution import Solution


class SolutionTest(unittest.TestCase):
    def test_case_1(self):
        nums1 = [1, 2, 3]
        nums2 = [2, 4, 6]
        expected_output = [[1, 3], [4, 6]]
        self.assertEqual(Solution().find_difference(nums1, nums2), expected_output)

    def test_case_2(self):
        nums1 = [1, 2, 3, 3]
        nums2 = [1, 1, 2, 2]
        expected_output = [[3], []]
        self.assertEqual(Solution().find_difference(nums1, nums2), expected_output)
