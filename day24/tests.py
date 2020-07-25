import unittest

from day24.solution import SymmetricBinaryTree


class SymmetricBinaryTreeTest(unittest.TestCase):
    def test_1(self):
        self.assertTrue(SymmetricBinaryTree([1, 2, 2, 3, 4, 4, 3]).is_symmetric())

    def test_2(self):
        self.assertFalse(SymmetricBinaryTree([1, 2, 2, None, 3, None, 3]).is_symmetric())
