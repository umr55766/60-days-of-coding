class Solution:
    def __init__(self):
        self.right_views = {}

    def rightSideView(self, root, level=0):
        if root is None:
            return list(self.right_views.values())

        self.right_views[level] = root.val

        if root.left:
            self.rightSideView(root.left, level+1)

        if root.right:
            self.rightSideView(root.right, level + 1)

        return list(self.right_views.values())


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right