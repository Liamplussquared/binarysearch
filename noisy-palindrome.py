# https://binarysearch.com/problems/Noisy-Palindrome
class Solution:
    def solve(self, s):
        clean = []
        for c in s:
            if c.islower():
                clean.append(c)

        return "".join(clean)[::-1] == "".join(clean)
