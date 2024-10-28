class Solution:
    def __init__(self):
        pass

    def count_bits(self, n):
        answer = [0] * (n+1)

        for number in range(1, n+1):
            if number % 2 == 0:
                answer[number] = answer[number//2]
            else:
                answer[number] = answer[number-1] + 1

        return answer