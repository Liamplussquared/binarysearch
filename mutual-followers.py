# https://binarysearch.com/problems/Mutual-Followers
class Solution:
    def solve(self, relations):
        res = set()
        seen = set()

        for a, b in relations:
            seen.add((a, b))
            if (b, a) in seen:
                res.add(a)
                res.add(b)

        res = list(set(res))
        res.sort()
        return res
