class Solution:
    def __init__(self):
        pass

    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        index_to_insert = 0
        current_index = 0

        while current_index < len(nums):
            if nums[current_index] != 0:
                nums[current_index], nums[index_to_insert] = nums[index_to_insert], nums[current_index]
                index_to_insert += 1
            current_index += 1

        while index_to_insert < len(nums):
            nums[index_to_insert] = 0
            index_to_insert += 1