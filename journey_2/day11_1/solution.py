class Solution:
    def max_vowels(self, string, substring_length):
        VOWELS = ["a", "e", "i", "o", "u"]
        if len(string) < substring_length:
            return len([char for char in string if char in VOWELS])

        substring = [char for char in string[0: substring_length]]
        current_vowels_count = vowels_count = len([char for char in substring if char.lower() in VOWELS])

        for index in range(substring_length, len(string)):
            current_vowels_count += 1 if string[index] in VOWELS else 0
            current_vowels_count -= 1 if substring[0] in VOWELS else 0

            del substring[0]
            substring.append(string[index])

            vowels_count = max(vowels_count, current_vowels_count)

        return vowels_count
