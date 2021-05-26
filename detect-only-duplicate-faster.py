# https://binarysearch.com/problems/Detect-the-Only-Duplicate-in-a-List
class Solution:
    def solve(self, nums):
        n, lst_sum = len(nums), sum(nums)
        act_sum = (n*(n-1)) / 2
        return abs(lst_sum - act_sum)
