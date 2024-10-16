class DuplicateDetector:
    def __init__(self, values):
        self.values = values

    def detect(self, lower_bound=None, higher_bound=None):
        lower_bound=1 if lower_bound is None else lower_bound
        higher_bound= len(self.values) - 1 if higher_bound is None else higher_bound

        if lower_bound == higher_bound:
            return lower_bound

        count = 0
        mid = (lower_bound + higher_bound) / 2
        for num in self.values:
            if num <= mid:
                count +=1

        if count > mid:
            return self.detect(lower_bound, int(mid))
        else:
            return self.detect(int(mid) + 1, higher_bound)
