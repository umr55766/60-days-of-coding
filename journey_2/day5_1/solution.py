class Solution:
    def __init__(self):
        pass

    def max_depth(self, root, depth=0):
        if root is None:
            return depth

        return max(self.max_depth(root.left, depth+1), self.max_depth(root.right, depth+1))


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right