from journey_1.day7.solution import index


class Solution:
    def __init__(self):
        self.ROOMS = []
        self.VISITED_ROOMS = []

    def can_visit_all_rooms(self, rooms):
        self.VISITED_ROOMS = [False for _ in rooms]
        self.ROOMS = rooms

        self.VISITED_ROOMS[0] = True

        for index in rooms[0]:
            if not self.VISITED_ROOMS[index]:
                self.visit(index)

        return all(self.VISITED_ROOMS)

    def visit(self, visiting_index):
        self.VISITED_ROOMS[visiting_index] = True

        for to_visit in self.ROOMS[visiting_index]:
            if not self.VISITED_ROOMS[to_visit]:
                self.visit(to_visit)
