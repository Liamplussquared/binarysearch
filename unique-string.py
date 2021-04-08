# https://binarysearch.com/problems/A-Unique-String
class Solution:
    def solve(self, s):
        lst = list(s)
        lst.sort()
        for i in range(1, len(lst)):
            if lst[i] == lst[i - 1]:
                return False
        return True
