class Solution:
    def __init__(self):
        self.maze = None
        self.directions = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]
        self.result = None

    def nearest_exit(self, maze, entrance, location = None, distance = None):
        if self.maze is None:
            self.maze = maze

        if location is not None and self.is_at_exit(location):
            return distance

        for direction in self.directions:
            if location is None:
                self.maze[entrance[0]][entrance[1]] = "*"
                next_location = [entrance[0] + direction[0], entrance[1] + direction[1]]
                if self.can_visit(next_location):
                    temp = self.nearest_exit(maze, entrance, next_location, 1)
                    self.result = min(self.result, temp) if self.result is not None and self.result!=-1 else temp
            else:
                self.maze[location[0]][location[1]] = "*"
                next_location = [location[0] + direction[0], location[1] + direction[1]]
                if self.can_visit(next_location):
                    temp = self.nearest_exit(maze, entrance, next_location, distance+1)
                    self.result = min(self.result, temp) if self.result is not None and self.result!=-1 else temp

        return self.result if self.result is not None else -1

    def is_at_exit(self, entrance):
        return (entrance[0] == 0 or entrance[0] == len(self.maze)-1) or (entrance[1] == 0 or entrance[1] == len(self.maze[0])-1)

    def can_visit(self, location):
        return (0 <= location[0] < len(self.maze)) and (0 <= location[1] < len(self.maze[0])) and self.maze[location[0]][location[1]] == "."
