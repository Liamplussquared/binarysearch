# https://binarysearch.com/problems/Check-Power-of-Two/editorials
class Solution:
    def solve(self, n):
        if n == 0:
            return False
        return str(bin(n))[2:].count("1") <= 1
