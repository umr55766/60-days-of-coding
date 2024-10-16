class MergeStringAlternatively:
    def __init__(self):
        pass

    def merge(self, string1, string2):
        merged = []
        min_length = min(len(string1), len(string2))

        # Merge characters from both strings alternately
        for i in range(min_length):
            merged.append(string1[i])
            merged.append(string2[i])

        # Add remaining characters from the longer string
        if len(string1) > min_length:
            merged.append(string1[min_length:])
        elif len(string2) > min_length:
            merged.append(string2[min_length:])

        return ''.join(merged)
