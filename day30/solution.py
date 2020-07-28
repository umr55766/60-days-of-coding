def jumpingOnClouds(c):
    return jump(c, 0, 0)


def jump(cloudSafetyIndexes, currentPosition, stepsTaken):
    if currentPosition >= len(cloudSafetyIndexes):
        return stepsTaken

    if currentPosition + 1 < len(cloudSafetyIndexes) and cloudSafetyIndexes[
        currentPosition + 1] == 0 and currentPosition + 2 < len(cloudSafetyIndexes) and cloudSafetyIndexes[
        currentPosition + 2] == 0:
        return min(jump(cloudSafetyIndexes, currentPosition + 1, stepsTaken + 1),
                   jump(cloudSafetyIndexes, currentPosition + 2, stepsTaken + 1))

    if currentPosition + 1 < len(cloudSafetyIndexes) and cloudSafetyIndexes[currentPosition + 1] == 0:
        return jump(cloudSafetyIndexes, currentPosition + 1, stepsTaken + 1)
    if currentPosition + 2 < len(cloudSafetyIndexes) and cloudSafetyIndexes[currentPosition + 2] == 0:
        return jump(cloudSafetyIndexes, currentPosition + 2, stepsTaken + 1)

    return stepsTaken
