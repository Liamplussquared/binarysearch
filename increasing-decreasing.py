# https://binarysearch.com/problems/Strictly-Increasing-or-Strictly-Decreasing
class Solution:
    def solve(self, nums):
        n = len(nums)
        if n < 2:
            return True
        elif nums[1] == nums[0]:
            return False

        # if true, increasing at start
        sign = nums[1] - nums[0] > 0

        for i in range(1, len(nums) - 1):
            diff = nums[i + 1] - nums[i]
            # print(diff)
            if sign != (diff > 0) or diff == 0:
                return False

        return True
