class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        pass

    def max_level_sum(self, root):
        level_sums = self.get_all_level_sums(root, {}, 1)

        max_sum = level_sums[1]
        max_sum_level = 1

        for key in level_sums:
            if level_sums[key] > max_sum:
                max_sum = level_sums[key]
                max_sum_level = key

        return max_sum_level

    def get_all_level_sums(self, root: TreeNode, level_sums : dict, level: int):
        if level in level_sums:
            level_sums[level] += root.val
        else:
            level_sums[level] = root.val

        if root.left:
            self.get_all_level_sums(root.left, level_sums, level + 1)

        if root.right:
            self.get_all_level_sums(root.right, level_sums, level + 1)

        return level_sums
