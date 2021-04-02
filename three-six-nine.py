# https://binarysearch.com/problems/3-6-9
class Solution:
    def solve(self, n):
        res = []
        for i in range(1, n+1):
            if i % 3 == 0 or any(t in str(i) for t in ['3','6','9']):
                res.append("clap")
            else:
                res.append(str(i))
        return res