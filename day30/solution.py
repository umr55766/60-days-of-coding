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


def repeatedString(s, n):
    countOfAsInString = len([1 for char in s if char == "a"])

    totalAsCount = (n // len(s)) * countOfAsInString
    totalAsCount += len([1 for char in s[0: (n % len(s))] if char == "a"])

    return totalAsCount


def minimumBribes(q):
    swapCount = 0

    for index, number in enumerate(q):
        if number - index > 3:
            return "Too chaotic"

    for i in range(len(q) - 1, 0, -1):
        if q[i] != i+1:
            if q[i - 1] == i+1:
                q[i - 1], q[i] = q[i], q[i - 1]
                swapCount += 1
            else:
                q[i - 2], q[i - 1] = q[i - 1], q[i - 2]
                q[i - 1], q[i] = q[i], q[i - 1]
                swapCount += 2

    return swapCount


def minimumSwaps(arr):
    swapCount = 0
    valueIndexes = {}

    for index, value in enumerate(arr):
        valueIndexes[value] = index

    for index in range(0, len(arr)):
        if arr[index] != index+1:
            sourceValue = arr[index]
            destinationValue = index+1

            sourceIndex = index
            destinationIndex = valueIndexes[destinationValue]

            arr[sourceIndex], arr[destinationIndex] = arr[destinationIndex], arr[sourceIndex]
            valueIndexes[sourceValue] = destinationIndex
            valueIndexes[destinationValue] = sourceIndex

            swapCount += 1

    return swapCount


def arrayManipulation(n, queries):
    values = {}

    for [a, b, k] in queries:
        if a in values:
            values[a] += k
        else:
            values[a] = k

        if b + 1 in values:
            values[b + 1] -= k
        else:
            values[b + 1] = -k

    indexes = sorted([key for key in values])

    maximum = 0
    sumUntilNow = 0
    for index in indexes:
        maximum = max(maximum, sumUntilNow + values[index])
        sumUntilNow += values[index]

    return maximum
