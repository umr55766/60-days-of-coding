class Solution:
    def __init__(self):
        pass

    def daily_temperatures(self, temperatures):
        results = [0] * len(temperatures)

        pending_indexes = []

        for current_index, current_temperature in enumerate(temperatures):

            while pending_indexes and current_temperature > temperatures[pending_indexes[-1]]:
                last_index = pending_indexes.pop()
                results[last_index] = current_index - last_index

            pending_indexes.append(current_index)

        return results