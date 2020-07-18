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
            root.left = self.insert_level_order(values, root.left, 2 * i + 1)
            root.right = self.insert_level_order(values, root.right, 2 * i + 2)

        return root


class RootToLeafNumbersSum:
    def __init__(self, values):
        self.tree = BinaryTree(values)
        self.sum = 0

    def aggregate(self, node, number_until_now):
        if node.right:
            self.aggregate(node.right, number_until_now + str(node.value))

        if node.left:
            self.aggregate(node.left, number_until_now + str(node.value))

        if not node.left and not node.right:
            self.sum += int(number_until_now + str(node.value))

    def sum(self):
        self.aggregate(self.tree.root, "")
        return self.sum
