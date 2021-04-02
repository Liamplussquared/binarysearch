# https://binarysearch.com/problems/Check-Palindrome
class Solution:
    def solve(self, s):
        return s == s[::-1]