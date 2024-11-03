class Solution:
    def __init__(self):
        pass

    def minimum_cost_stairs(self, stairs_cost):
        second_last_stair = stairs_cost[0]
        last_stair = stairs_cost[1]

        for index in range(2, len(stairs_cost)):
            second_last_stair, last_stair = last_stair, min(second_last_stair, last_stair) + stairs_cost[index]

        return min(last_stair, second_last_stair)