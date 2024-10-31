class Solution:
    def is_subsequence(self, subsequence: str, main_string: str) -> bool:
        if len(subsequence) == 0:
            return True

        if len(main_string) == 0:
            return False

        subsequence_index = 0

        for char in main_string:
            if char == subsequence[subsequence_index]:
                subsequence_index += 1

            if subsequence_index == len(subsequence) and subsequence_index != 0:
                return True

        return False