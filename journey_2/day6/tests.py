import unittest

from journey_2.day6.solution import Solution, TreeNode


class SolutionTest(unittest.TestCase):
    def test_1(self):
        self.root = TreeNode(4)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(7)
        self.root.left.left = TreeNode(1)
        self.root.left.right = TreeNode(3)

        result = Solution().search_bst(self.root, 2)
        self.assertEqual(result.val, 2)
        self.assertEqual(result.left.val, 1)
        self.assertEqual(result.right.val, 3)

    def test_2(self):
        self.root = TreeNode(4)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(7)
        self.root.left.left = TreeNode(1)
        self.root.left.right = TreeNode(3)

        result = Solution().search_bst(self.root, 5)
        self.assertIsNone(result)
