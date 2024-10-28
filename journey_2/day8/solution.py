import math


class Solution:
    def __init__(self):
        pass

    def unique_paths(self, m ,n):
        return math.comb((m+n-2), n-1)