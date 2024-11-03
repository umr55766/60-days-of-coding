class Solution:
    def __init__(self):
        pass

    def get_longest_subsequence_length(self, sequence1, sequence2):
        lengths = [[0] * (len(sequence2)+1) for _ in range(len(sequence1)+1)]

        for index1 in range(1, len(sequence1)+1):
            for index2 in range(1, len(sequence2)+1):
                if sequence1[index1-1] == sequence2[index2-1]:
                    lengths[index1][index2] = lengths[index1-1][index2-1] + 1
                else:
                    lengths[index1][index2] = max(lengths[index1 - 1][index2], lengths[index1][index2 - 1])

        return lengths[len(sequence1)][len(sequence2)]
