# https://binarysearch.com/problems/Consecutive-Ones
class Solution:
    def solve(self, nums):
        seen = False
        c, distance = 0, []

        for i in range(len(nums)):
            if nums[i] == 1:
                distance.append(c)
                if c > 0:
                    return False
                seen = True
            elif seen:
                c += 1

        return True
