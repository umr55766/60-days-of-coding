from journey_1.day5.solution import start_index


class Solution:
    def __init__(self):
        pass

    def method_name(self, array, length):
        running_sum = max_sum = sum(array[:length])
        front_index = 0
        rear_index = length

        while rear_index < len(array):
            running_sum += array[rear_index] - array[front_index]
            max_sum = max(max_sum, running_sum)
            rear_index += 1
            front_index += 1

        return max_sum / length