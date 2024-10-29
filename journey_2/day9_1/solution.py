class Solution:
    def __init__(self):
        pass

    def daily_temperatures(self, temperatures):
        results = [0] * len(temperatures)

        indexes_pending_update = []

        for index, temperature in enumerate(temperatures):

            while indexes_pending_update and temperature > temperatures[indexes_pending_update[-1]]:
                index_pending_update = indexes_pending_update.pop()
                results[index_pending_update] = index - index_pending_update

            indexes_pending_update.append(index)

        return results