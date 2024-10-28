import unittest

from journey_2.day8_3.solution import Solution


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.trie = Solution()

    def test_insert_and_search(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"))  # Should return True
        self.assertFalse(self.trie.search("app"))    # Should return False
        self.assertTrue(self.trie.starts_with("app"))  # Should return True
        self.trie.insert("app")
        self.assertTrue(self.trie.search("app"))      # Should return True

    def test_startsWith(self):
        self.trie.insert("banana")
        self.assertTrue(self.trie.starts_with("ban"))   # Should return True
        self.assertFalse(self.trie.starts_with("bat"))   # Should return False

    def test_edge_cases(self):
        self.assertFalse(self.trie.search(""))          # Should return False for empty search
        self.assertTrue(self.trie.starts_with(""))      # Should return True for empty prefix

    def test_insert_duplicates(self):
        self.trie.insert("orange")
        self.trie.insert("orange")  # Inserting the same word again
        self.assertTrue(self.trie.search("orange"))  # Should still return True
