# https://binarysearch.com/problems/Rotation-of-Another-String
class Solution:
    def solve(self, s0, s1):
        return s0 in (s1+s1) and len(s0)==len(s1)