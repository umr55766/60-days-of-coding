class Solution:
    def __init__(self):
        pass

    def num_of_islands(self, grid):
        LAND = "1"
        WATER = "0"
        island_count = 0
        rows, cols = len(grid), len(grid[0] if grid else [])

        def record_island_iterative(row, col):
            stack = [(row, col)]
            while stack:
                r, c = stack.pop()
                if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == WATER:
                    continue

                grid[r][c] = WATER

                stack.append((r, c + 1))
                stack.append((r + 1, c))
                stack.append((r, c - 1))
                stack.append((r - 1, c))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == LAND:
                    island_count += 1
                    record_island_iterative(row, col)

        return island_count