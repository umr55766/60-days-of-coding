import heapq


class MaxHeapObj(object):
    def __init__(self, val): self.val = val

    def __lt__(self, other): return self.val > other.val

    def __eq__(self, other): return self.val == other.val

    def __str__(self): return str(self.val)


class KSmallestSumPairs:
    def __init__(self, first_pairs, second_pairs):
        self.first_pairs = first_pairs
        self.second_pairs = second_pairs

    def get(self, k):
        if not self.first_pairs or not self.second_pairs or not k:
            return []

        target = []
        count = 0
        for n1 in self.first_pairs:
            for n2 in self.second_pairs:
                sum = n1 + n2
                if (count < k):
                    heapq.heappush(
                        target,
                        MaxHeapObj((sum, [n1, n2]))
                    )
                else:
                    if (target[0].val[0] > sum):
                        heapq.heappop(target)
                        heapq.heappush(
                            target,
                            MaxHeapObj((sum, [n1, n2]))
                        )
                count += 1

        final = []
        for _ in range(k):
            if len(target) > 0:
                x, y = heapq.heappop(target).val
                final.extend([y])

        return list(reversed(final))