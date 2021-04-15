# https://binarysearch.com/room/Hash-Table-JDCg7XaPN5
class Solution:
    def solve(self, nums):
        occ = {}
        for n in nums:
            if n in occ:
                occ[n] += 1
            else:
                occ[n] = 1
        
        num_occ = list(occ.values())
        return len(set(num_occ)) == len(num_occ)
