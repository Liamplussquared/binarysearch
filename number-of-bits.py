# https://binarysearch.com/problems/Number-of-Bits
class Solution:
    def solve(self, n):
        return (bin(n).count('1'))
        