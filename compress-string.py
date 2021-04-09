# https://binarysearch.com/problems/Compress-String
"""
Naive string appending is slow in python
https://waymoot.org/home/python_string/
"""
class Solution:
    def solve(self, s):
        j, res = 0, [s[0]]
        for i in range(1, len(s)): 
            if res[j] != s[i]:
                res.append(s[i])
                j += 1
        return ''.join(res)