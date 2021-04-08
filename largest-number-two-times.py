# https://binarysearch.com/problems/Largest-Number-By-Two-Times
class Solution:
    def solve(self, nums):
        nums.sort()
        return nums[-1] > 2*nums[-2]
        