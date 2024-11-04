class Solution:
    def __init__(self):
        pass

    def reverse_vowels(self, string):
        string = list(string)
        low, high = 0, len(string) - 1

        while low < high:
            while low < high and string[low] not in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:
                low += 1

            while low < high and string[high] not in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:
                high -= 1

            string[low], string[high] = string[high], string[low]
            low += 1
            high -= 1

        return "".join(string)