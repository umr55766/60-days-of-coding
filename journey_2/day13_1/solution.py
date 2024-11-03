class Solution:
    def __init__(self):
        pass

    def get_longest_subsequence_length(self, sequence1, sequence2):
        if len(sequence1) < len(sequence2):
            sequence1, sequence2 = sequence2, sequence1

        previous_row = [0] * (len(sequence2) + 1)
        current_row = [0] * (len(sequence2) + 1)

        for index1 in range(1, len(sequence1) + 1):
            for index2 in range(1, len(sequence2) + 1):
                if sequence1[index1 - 1] == sequence2[index2 - 1]:
                    current_row[index2] = previous_row[index2 - 1] + 1
                else:
                    current_row[index2] = max(previous_row[index2], current_row[index2 - 1])

            previous_row, current_row = current_row, previous_row

        return previous_row[len(sequence2)]
