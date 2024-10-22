class Solution:
    def __init__(self):
        pass

    def method_name(self, param):
        return param

    def rightSideView(self, root):
        if root is None:
            return []

        return [root.val] + self.rightSideView(root.right)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right