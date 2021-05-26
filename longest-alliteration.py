# https://binarysearch.com/problems/Longest-Alliteration
class Solution:
    def solve(self, words):
        if not words:
            return 0

        n, count, max_count = len(words), 1, 1

        for i in range(1, n):
            if words[i][0] == words[i - 1][0]:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 1

        return max_count
