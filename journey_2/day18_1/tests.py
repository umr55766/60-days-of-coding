import unittest

from journey_2.day18_1.solution import Solution, TreeNode


class SolutionTest(unittest.TestCase):
    def test_case1(self):
        root1 = list_to_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4])
        root2 = list_to_tree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])
        self.assertTrue(Solution().have_similar_leaf(root1, root2))

    def test_case2(self):
        root1 = list_to_tree([1, 2, 3])
        root2 = list_to_tree([1, 3, 2])
        self.assertFalse(Solution().have_similar_leaf(root1, root2))

    def test_single_node_similar(self):
        root1 = list_to_tree([1])
        root2 = list_to_tree([1])
        self.assertTrue(Solution().have_similar_leaf(root1, root2))

    def test_single_node_different(self):
        root1 = list_to_tree([1])
        root2 = list_to_tree([2])
        self.assertFalse(Solution().have_similar_leaf(root1, root2))

    def test_large_trees_similar(self):
        root1 = list_to_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4])
        root2 = list_to_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4])
        self.assertTrue(Solution().have_similar_leaf(root1, root2))

    def test_large_trees_different(self):
        root1 = list_to_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4])
        root2 = list_to_tree([3, 5, 1, 6, 2, 9, 7, None, None, 4, 8])
        self.assertFalse(Solution().have_similar_leaf(root1, root2))


def list_to_tree(lst, index=0):
    """Helper function to convert a list to a binary tree structure."""
    if index >= len(lst) or lst[index] is None:
        return None
    root = TreeNode(lst[index])
    root.left = list_to_tree(lst, 2 * index + 1)
    root.right = list_to_tree(lst, 2 * index + 2)
    return root
