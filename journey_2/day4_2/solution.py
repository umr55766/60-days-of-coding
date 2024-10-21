class Solution:
    def __init__(self):
        self.stack = []

    def ping(self, time):
        while self.stack and (time - self.stack[0]) > 3000:
            del self.stack[0]
        self.stack.append(time)
        return len(self.stack)