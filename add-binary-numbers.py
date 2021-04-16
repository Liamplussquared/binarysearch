# https://binarysearch.com/problems/Add-Binary-Numbers
# Using built in functions, return bin(int(a, 2) + int(b, 2))[2:]
class Solution:
    def solve(self, a, b):
        decA, decB = 0, 0
        a, b = a[::-1], b[::-1]

        for i in range(len(a)):
            decA += int(a[i]) * (2 ** i)
        for i in range(len(b)):
            decB += int(b[i]) * (2 ** i)

        return str(bin(decA + decB)[2:])
