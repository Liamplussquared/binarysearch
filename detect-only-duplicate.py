# https://binarysearch.com/problems/Detect-the-Only-Duplicate-in-a-List
class Solution:
    def solve(self, nums):
        n = len(nums)
        count = [0 for i in range(n)]

        for num in nums:
            count[num] += 1
            if count[num] > 1:
                return num

        return -1
