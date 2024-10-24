from collections import deque


class Solution:
    def nearest_exit(self, maze, entrance, location = None, distance = None):
        directions = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]
        maze[entrance[0]][entrance[1]] = "*"
        queue = deque([[entrance[0], entrance[1], 0]])

        while queue:
            i, j, distance = queue.popleft()

            if self.is_at_exit(maze, i, j) and [i, j] != entrance:
                return distance

            for x, y in directions:
                x, y = x + i, y + j

                if self.can_visit(maze, x, y):
                    maze[x][y] = "*"
                    queue.append((x, y, distance + 1))

        return -1

    def is_at_exit(self, maze, x, y):
        return (x in (0, len(maze) - 1) or y in (0, len(maze[0]) - 1))

    def can_visit(self, maze, x, y):
        return x in range(0, len(maze)) and y in range(0, len(maze[0])) and maze[x][y] == "."