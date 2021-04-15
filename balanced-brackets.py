# https://binarysearch.com/problems/Balanced-Brackets
class Solution:
    def solve(self, s):
        stack = []
        n = len(stack)

        for bracket in s:
            if bracket == "(":
                stack.append(bracket)
                n += 1
            elif bracket == ")":
                if n == 0 or stack.pop() != "(":
                    return False
                n -= 1

        return len(stack) == 0
