import unittest

from journey_2.day18_2.solution import Solution, TreeNode


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        # Tree: [1,7,0,7,-8,null,null]
        root = TreeNode(1)
        root.left = TreeNode(7)
        root.right = TreeNode(0)
        root.left.left = TreeNode(7)
        root.left.right = TreeNode(-8)
        self.assertEqual(self.solution.max_level_sum(root), 2)

    def test_example_2(self):
        # Tree: [989,null,10250,98693,-89388,null,null,null,-32127]
        root = TreeNode(989)
        root.right = TreeNode(10250)
        root.right.left = TreeNode(98693)
        root.right.right = TreeNode(-89388)
        root.right.right.right = TreeNode(-32127)
        self.assertEqual(self.solution.max_level_sum(root), 2)

    def test_single_node(self):
        # Tree: [5]
        root = TreeNode(5)
        self.assertEqual(self.solution.max_level_sum(root), 1)

    def test_negative_values(self):
        # Tree: [-1, -2, -3, -4, -5]
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-3)
        root.left.left = TreeNode(-4)
        root.left.right = TreeNode(-5)
        self.assertEqual(self.solution.max_level_sum(root), 1)

    def test_multiple_levels_with_same_sum(self):
        # Tree: [1, 2, 3, 4, 5]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        # Level 1 sum = 1, Level 2 sum = 5, Level 3 sum = 9
        self.assertEqual(self.solution.max_level_sum(root), 3)
