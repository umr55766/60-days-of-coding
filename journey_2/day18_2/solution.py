from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        pass

    def max_level_sum(self, root):
        if not root:
            return 0

        max_sum = float('-inf')
        max_level = 1
        current_level = 1
        queue = deque([root])

        while queue:
            level_sum = 0
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Update max level if this level's sum is greater
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level

            current_level += 1

        return max_level