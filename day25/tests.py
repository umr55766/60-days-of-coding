import unittest

from day11.solution import BinaryTree


class ValidateBinaryTreeTest(unittest.TestCase):
    def test_1(self):
        self.assertTrue(BinaryTree([2, 1, 3]).validate())

    def test_2(self):
        self.assertFalse(BinaryTree([5, 1, 4, None, None, 3, 6]).validate())
