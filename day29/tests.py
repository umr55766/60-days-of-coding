import unittest

from day29.solution import MinStack


class MinStackTest(unittest.TestCase):
    def test_1(self):
        min_stack = MinStack()
        min_stack.push(-2)
        min_stack.push(0)

        min_stack.push(-3)
        self.assertEqual(-3, min_stack.get_min())

        min_stack.pop()
        self.assertEqual(0, min_stack.top())

        self.assertEqual(-2, min_stack.get_min())
