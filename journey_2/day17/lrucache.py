from collections import OrderedDict


class LRUCache:
    NOT_FOUND = -1
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def put(self, key, value):
        pass

    def get(self, key):
        if key not in self.cache:
            return self.NOT_FOUND

        self.cache.move_to_end(key)

        return self.cache[key]