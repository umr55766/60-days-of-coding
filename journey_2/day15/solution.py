from collections import deque


class Solution:
    def __init__(self):
        pass

    def predict_victory_party(self, senate):
        radiant_queue = deque()
        dire_queue = deque()

        for index, senator in enumerate(senate):
            if senator == "R":
                radiant_queue.append(index)
            else:
                dire_queue.append(index)

        while radiant_queue and dire_queue:
            radiant = radiant_queue.popleft()
            dire = dire_queue.popleft()

            if radiant < dire:
                radiant_queue.append(radiant + len(senate))
            else:
                dire_queue.append(dire + len(senate))

        return "Radiant" if radiant_queue else "Dire"
