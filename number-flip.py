# https://binarysearch.com/problems/123-Number-Flip
class Solution:
    def solve(self, n):
        m = str(n)

        for i in range(len(m)):
            if m[i] != "3":
                return int("".join(m[0:i] + "3" + m[i + 1 :]))

        return n
