class Solution:
    def __init__(self):
        pass

    def search_bst(self, root, param):
        if root is None:
            return None

        if root.val == param:
            return root

        return self.search_bst(root.left, param) or self.search_bst(root.right, param)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
