# https://binarysearch.com/problems/Equivalent-Pairs
class Solution:
    def solve(self, nums):
        table = {}
        res = 0

        for num in nums:
            if num in table:
                res += table[num]
                table[num] += 1
            else:
                table[num] = 1

        return res
