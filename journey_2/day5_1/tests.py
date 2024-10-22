import unittest

from journey_2.day5_1.solution import Solution, TreeNode


class SolutionTest(unittest.TestCase):
    def test_1(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        # Expected output: 3
        self.assertEqual(Solution().max_depth(root), 3)

    def test_2(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        # Expected output: 2
        self.assertEqual(Solution().max_depth(root), 2)
