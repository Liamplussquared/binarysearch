# https://binarysearch.com/problems/Pascal's-Triangle/submissions/4441799
class Solution:
    def solve(self, n):
        pascal = [[1], [1,1]]
        i, temp = 2, []

        while i <= n:
            pascal.append(self.calc(pascal[i-1]))
            i += 1

        return pascal[n]
    
    def calc(self, lst):
        res = [1]
        for i in range(len(lst)-1):
            res.append(lst[i]+lst[i+1])
        res.append(1)
        return res
