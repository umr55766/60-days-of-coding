class MinStackNode:
    def __init__(self, x=None):
        self.val = x
        self.min = x
        self.next = None


class MinStack:
    def __init__(self):
        self.top_node = None

    def push(self, x):
        temp = MinStackNode(x)
        if self.top_node is not None:
            temp.next = self.top_node
            if x > self.top_node.min:
                temp.min = self.top_node.min
        self.top_node = temp

    def pop(self):
        if self.top_node is None:
            return None
        temp = self.top_node
        self.top_node = temp.next

    def top(self):
        if self.top_node is None:
            return None

        return self.top_node.val

    def get_min(self):
        if self.top_node is None:
            return None

        return self.top_node.min
