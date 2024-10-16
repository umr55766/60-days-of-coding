class BreakDown:
    def __init__(self, string, words):
        self.string = string
        self.words = words

    def is_breakable(self, string=None):
        if string is None:
            string = self.string

        if string == "":
            return True

        for word in self.words:
            if string.startswith(word):
                return self.is_breakable(string.replace(word, ""))

        return False
