# https://binarysearch.com/problems/Roomba
class Solution:
    def solve(self, moves, x, y):
        for move in moves:
            if move == "NORTH":
                y -= 1
            elif move == "SOUTH":
                y += 1
            elif move == "EAST":
                x -= 1
            elif move == "WEST":
                x += 1

        return (x, y) == (0, 0)
