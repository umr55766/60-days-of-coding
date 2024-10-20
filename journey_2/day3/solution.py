class Solution:
    def largestAltitude(self, gains):
        highest_altitude = 0
        altitude = 0

        for gain in gains:
            altitude += gain
            if altitude > highest_altitude:
                highest_altitude = altitude

        return highest_altitude