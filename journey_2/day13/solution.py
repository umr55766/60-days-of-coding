class Solution:
    def __init__(self):
        pass

    def get_expiry_minutes(self, oranges):
        newly_rottens = []
        ROTTEN = 2
        FRESH = 1

        for row in range(len(oranges)):
            for col in range(len(oranges[0])):
                if oranges[row][col] == ROTTEN:
                    newly_rottens.append([row, col])

        minutes = 0

        while len(newly_rottens) != 0:
            will_rottens = []

            for newly_rotten in newly_rottens:
                if newly_rotten[1] < len(oranges[0])-1 and oranges[newly_rotten[0]][newly_rotten[1]+1] == FRESH:
                    will_rottens.append([newly_rotten[0], newly_rotten[1]+1])

                if newly_rotten[0] < len(oranges)-1 and oranges[newly_rotten[0]+1][newly_rotten[1]] == FRESH:
                    will_rottens.append([newly_rotten[0]+1, newly_rotten[1]])

                if newly_rotten[1] > 0 and oranges[newly_rotten[0]][newly_rotten[1]-1] == FRESH:
                    will_rottens.append([newly_rotten[0], newly_rotten[1]-1])

                if newly_rotten[0] > 0 and oranges[newly_rotten[0]-1][newly_rotten[1]] == FRESH:
                    will_rottens.append([newly_rotten[0]-1, newly_rotten[1]])

            if len(will_rottens) == 0:
                break

            minutes += 1
            for will_rotten in will_rottens:
                oranges[will_rotten[0]][will_rotten[1]] = ROTTEN

            newly_rottens = will_rottens

        for row in range(len(oranges)):
            for col in range(len(oranges[0])):
                if oranges[row][col] == FRESH:
                    return -1

        return minutes