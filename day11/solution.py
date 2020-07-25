class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, values):
        self.root = self.insert_level_order(values, None, 0)

    def insert_level_order(self, values, root, i):
        if i < len(values):
            temp = BinaryTreeNode(values[i])
            root = temp
            if 2 * i + 1 < len(values) and values[2 * i + 1] is not None:
                root.left = self.insert_level_order(values, root.left, 2 * i + 1)
            if 2 * i + 2 < len(values) and values[2 * i + 2] is not None:
                root.right = self.insert_level_order(values, root.right, 2 * i + 2)

        return root

    def _validate(self, node):
        if node is None or (node.left is None and node.right is None):
            return True

        if (node.left is None or node.left.value <= node.value) and (node.right is None or node.right.value >= node.value):
            return self._validate(node.left) and self._validate(node.right)

        return False

    def validate(self):
        return self._validate(self.root)


class RootToLeafNumbersSum:
    def __init__(self, values):
        self.tree = BinaryTree(values)
        self._sum = 0

    def aggregate(self, node, number_until_now):
        if node.right:
            self.aggregate(node.right, number_until_now + str(node.value))

        if node.left:
            self.aggregate(node.left, number_until_now + str(node.value))

        if not node.left and not node.right:
            self._sum += int(number_until_now + str(node.value))

    def sum(self):
        self.aggregate(self.tree.root, "")
        return self._sum
