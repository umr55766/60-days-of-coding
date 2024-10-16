class MergeStringAlternatively:
    def __init__(self):
        pass

    def merge(self, string1, string2):
        result = ""
        index = 0
        while index < min(len(string1), len(string2)):
            result += string1[index] + string2[index]
            index += 1

        result += string1[index:]
        result += string2[index:]

        return result
