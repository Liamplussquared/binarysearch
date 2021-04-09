# https://binarysearch.com/problems/Rotate-List-Left-by-K
class Solution:
    def solve(self, nums, k):
        if len(nums) == 0:
            return nums

        return nums[k:] + nums[0:k]
