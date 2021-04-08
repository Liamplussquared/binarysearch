class Solution:
    def solve(self, a, b):
        res = []
        n, m = len(a), len(b)
        i, j = 0, 0

        while i < n and j < m:
            a_ele, b_ele = a[i], b[j]
            if a_ele > b_ele:
                res.append(b_ele)
                j += 1
            else:
                res.append(a_ele)
                i += 1    

        return res + a[i:] + b[j:]