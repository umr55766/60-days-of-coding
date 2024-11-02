class Solution:
    def __init__(self):
        pass

    def is_occurences_unique(self, numbers):
        number_count_dictionary = {}

        for number in numbers:
            if number in number_count_dictionary:
                number_count_dictionary[number] += 1
            else:
                number_count_dictionary[number] = 1

        return len(number_count_dictionary.values()) == len(set(number_count_dictionary.values()))