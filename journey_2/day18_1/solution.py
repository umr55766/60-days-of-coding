from itertools import zip_longest

from setuptools.dist import sequence


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        pass

    def have_similar_leaf(self, root1, root2):
        def leaf_generator(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                else:
                    yield from leaf_generator(node.left)
                    yield from leaf_generator(node.right)

        for val1, val2 in zip_longest(leaf_generator(root1), leaf_generator(root2), fillvalue=None):
            if val1 != val2:
                return False
        return True
