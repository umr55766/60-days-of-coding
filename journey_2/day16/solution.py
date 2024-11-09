class Solution:
    def __init__(self):
        pass

    def is_close(self, word1, word2):
        if len(word1) != len(word2):
            return False

        word1_dict = {}
        for char in word1:
            if char in word1_dict:
                word1_dict[char] += 1
            else:
                word1_dict[char] = 0

        word2_dict = {}
        for char in word2:
            if char in word2_dict:
                word2_dict[char] += 1
            else:
                word2_dict[char] = 0

        return sorted(set(word1_dict.keys())) == sorted(set(word2_dict.keys())) and sorted(
            word1_dict.values()) == sorted(word2_dict.values())