# https://binarysearch.com/problems/Pascal's-Triangle
class Solution:
    def solve(self, n):
        res = []
        for i in range(0, n + 1):
            res.append(math.comb(n, i))
        return res
