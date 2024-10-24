from heapq import heappush, heappushpop


class Solution:
    def __init__(self):
        pass

    def find_kth_largest(self, nums, k):
        heap = []

        for i in range(k):
            heappush(heap, nums[i])

        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heappushpop(heap, nums[i])

        return heap[0]