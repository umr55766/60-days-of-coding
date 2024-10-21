class Solution:
    def __init__(self):
        pass

    def find_difference(self, nums1, nums2):
        return [[_ for _ in set(nums1) if _ not in nums2], [_ for _ in set(nums2) if _ not in nums1]]