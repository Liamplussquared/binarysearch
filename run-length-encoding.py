# https://binarysearch.com/problems/Run-Length-Encoding
class Solution:
    def solve(self, s):
        res = ""
        counter = 1
        for i in range(len(s)-1):
            if s[i+1] == s[i]:
                counter += 1
            else:
                res += str(counter)+s[i]
                counter = 1
        res += str(counter)+s[-1]
        return res
                