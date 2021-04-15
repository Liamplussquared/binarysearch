# https://binarysearch.com/problems/Leaderboard
class Solution:
    def solve(self, nums):
        res = list(set(nums))
        res.sort(reverse=True)

        temp, rankings = 0, {}
        for r in res:
            rankings[r] = temp
            temp += 1

        lst = []
        for n in nums:
            lst.append(rankings[n])

        return lst
