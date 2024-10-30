class Solution:
    def __init__(self):
        self.historical_spans = []

    def next(self, price: int) -> int:
        result = 1

        while self.historical_spans and self.historical_spans[-1][0] <= price:
            result += self.historical_spans.pop()[1]

        self.historical_spans.append((price, result))

        return result
