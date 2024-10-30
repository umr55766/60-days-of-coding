from operator import itemgetter


class Solution:
    def find_min_arrow_shots(self, points):
        points.sort(key = itemgetter(1))

        arrows = 1
        previous_balloon_end = points[0][1]

        for index in range(1, len(points)):
            if points[index][0] > previous_balloon_end:
                arrows += 1
                previous_balloon_end = points[index][1]

        return arrows