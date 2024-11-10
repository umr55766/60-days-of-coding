# from collections import OrderedDict
#
#
# Using OrderedDict
# class LRUCache:
#     NOT_FOUND = -1
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.cache = OrderedDict()
#
#     def put(self, key, value):
#         if key in self.cache:
#             self.cache.move_to_end(key)
#         self.cache[key] = value
#
#         if len(self.cache) > self.capacity:
#             self.cache.popitem(last=False)
#
#     def get(self, key):
#         if key not in self.cache:
#             return self.NOT_FOUND
#
#         self.cache.move_to_end(key)
#
#         return self.cache[key]


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Dictionary to hold key-node mappings
        # Initialize dummy head and tail nodes
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Remove node from the linked list."""
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def _add_to_front(self, node: Node):
        """Add node right after head."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move the accessed node to the front of the list
        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the existing node and move it to the front
            self._remove(self.cache[key])
        elif len(self.cache) == self.capacity:
            # Remove the least recently used node (node before the tail)
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

        # Create a new node and add it to the front of the list
        new_node = Node(key, value)
        self._add_to_front(new_node)
        self.cache[key] = new_node