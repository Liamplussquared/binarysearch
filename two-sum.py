# https://binarysearch.com/problems/Sum-of-Two-Numbers
class Solution:
    def solve(self, nums, k):
        elements = set()
        for i in nums:
            target = k - i
            if target in elements:
                return True
            else:
                elements.add(i)
        return False
