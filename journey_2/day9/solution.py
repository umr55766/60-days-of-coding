from operator import itemgetter


class Solution:
    def __init__(self):
        pass

    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=itemgetter(1))
        number_of_intervals = len(intervals)

        previous_meeting_endtime = intervals[0][1]
        number_of_non_overlapping_intervals = 1

        for index in range(1, number_of_intervals):
            if intervals[index][0] >= previous_meeting_endtime:
                number_of_non_overlapping_intervals += 1
                previous_meeting_endtime = intervals[index][1]

        return number_of_intervals - number_of_non_overlapping_intervals
