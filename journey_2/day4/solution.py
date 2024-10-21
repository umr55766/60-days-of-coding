class Solution:
    def __init__(self):
        pass

    def asteroid_collision(self, asteroids):
        stack = []
        for asteroid in asteroids:
            while stack and self.is_colliding(asteroid, stack):
                if self.is_dominating(asteroid, stack):
                    stack.pop()
                    continue
                elif self.is_going_headon(asteroid, stack):
                    stack.pop()
                break
            else:
                stack.append(asteroid)

        return stack

    def is_going_headon(self, asteroid, stack):
        return stack[-1] == -asteroid

    def is_dominating(self, asteroid, stack):
        return stack[-1] < -asteroid

    def is_colliding(self, asteroid, stack):
        return asteroid < 0 < stack[-1]
