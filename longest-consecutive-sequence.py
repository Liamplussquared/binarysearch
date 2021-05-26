# https://binarysearch.com/problems/Longest-Consecutive-Sequence
class Solution:
    def solve(self, nums):
        if not nums:
            return 0

        nums.sort()
        n, count, max_count = len(nums), 1, 1

        for i in range(1, n):
            curr, prev = nums[i], nums[i - 1]
            if curr - prev == 1:
                count += 1
                if count > max_count:
                    max_count = count
            elif curr - prev == 0:
                pass
            else:
                count = 1

        return max_count
