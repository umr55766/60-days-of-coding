from journey_1.day11.solution import BinaryTree


class SymmetricBinaryTree:
    def __init__(self, values):
        self.tree = BinaryTree(values)

    def is_similar(self, left_node, right_node):
        if left_node is None and right_node is None:
            return True

        if left_node is None or right_node is None:
            return False

        if left_node.value != right_node.value:
            return False

        return self.is_similar(right_node.left, left_node.right) and self.is_similar(right_node.right, left_node.left)

    def is_symmetric(self):
        if self.tree.root is None:
            return True

        return self.is_similar(self.tree.root.left, self.tree.root.right)
