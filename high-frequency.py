# https://binarysearch.com/problems/High-Frequency
class Solution:
    def solve(self, nums):
        if not nums:
            return 0

        mp = {}
        for num in nums:
            if num not in mp:
                mp[num] = 1
            else:
                mp[num] += 1

        return max(mp.values())
