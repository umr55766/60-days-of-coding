class Solution:
    def max_vowels(self, string, substring_length):
        VOWELS = {"a", "e", "i", "o", "u"}

        current_vowels_count = sum(1 for char in string[:substring_length] if char in VOWELS)
        max_vowels_count = current_vowels_count

        for i in range(substring_length, len(string)):
            if string[i] in VOWELS:
                current_vowels_count += 1

            if string[i - substring_length] in VOWELS:
                current_vowels_count -= 1

            max_vowels_count = max(max_vowels_count, current_vowels_count)

        return max_vowels_count
