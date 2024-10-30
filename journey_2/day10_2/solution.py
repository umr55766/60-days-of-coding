class Solution:
    def __init__(self):
        pass

    def combination_sum(self, length, aggregate):

        if length > aggregate:
            return []

        result = []

        def dfs(index, combination):
            if len(combination) == length:
                if sum(combination) == aggregate:
                    result.append(combination)
                return

            for digit in range(index, 10):
                if sum(combination) + digit <= aggregate:
                    dfs(digit+1, combination + [digit])
                if sum(combination) + digit > aggregate:
                    return

        dfs(1, [])

        return result