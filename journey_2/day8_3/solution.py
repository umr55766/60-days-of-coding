class Solution:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str, node=None) -> None:
        if len(word) == 0:
            if node is not None:
                node["isWord"] = True
            return

        node = node if node is not None else self.trie

        if word[0] not in node:
            node[word[0]] = {
                "isWord": False
            }

        self.insert(word[1:], node[word[0]])

    def search(self, word: str, node=None) -> bool:
        node = self.trie if node is None else node

        if len(word) == 0:
            return "isWord" in node and node["isWord"]

        if word[0] not in node:
            return False

        return self.search(word[1:], node[word[0]])

    def starts_with(self, prefix: str, node=None) -> bool:
        node = self.trie if node is None else node

        if len(prefix) == 0:
            return True

        if prefix[0] not in node:
            return False

        return self.starts_with(prefix[1:], node[prefix[0]])