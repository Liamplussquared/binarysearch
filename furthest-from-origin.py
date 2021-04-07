# https://binarysearch.com/problems/Furthest-From-Origin
class Solution:
    def solve(self, s):
        distance = 0
        num_l, num_r, num_misc = 0, 0, 0
        for letter in s:
            if letter == 'L':
                num_l += 1
            elif letter == 'R':
                num_r += 1
            elif letter == '?':
                num_misc += 1
   
        if num_l > num_r:
            return num_l - num_r + num_misc
        elif num_l < num_r:
            return num_r - num_l + num_misc
        else:
            return num_misc
