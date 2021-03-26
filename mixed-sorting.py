#https://binarysearch.com/problems/Mixed-Sorting
class Solution:
    def solve(self, nums):
        even = sorted([i for i in nums if int(i)%2==0])
        odd = sorted([i for i in nums if int(i)%2!=0], reverse=True)

        eC, oC = 0, 0 
        for i in range(len(nums)):
            num = nums[i]
            if num%2==0:
                nums[i] = even[eC]
                eC+=1
            else:
                nums[i] = odd[oC]
                oC+=1

        return nums