import unittest

from journey_2.day5_2.solution import Solution, TreeNode


class SolutionTest(unittest.TestCase):
    def test_example_1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(4)
        self.assertEqual(Solution().rightSideView(root), [1, 3, 4])

    def test_example_2(self):
        root = TreeNode(1)
        root.right = TreeNode(3)
        self.assertEqual(Solution().rightSideView(root), [1, 3])

    def test_example_3(self):
        root = None
        self.assertEqual(Solution().rightSideView(root), [])
