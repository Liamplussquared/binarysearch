# https://binarysearch.com/problems/Transpose-of-a-Matrix
"""
*, ** -> unpacking operators
zip() -> maps index of iterables together
"""
class Solution:
    def solve(self, matrix):
        zipped = zip(*matrix)
        return [list(col) for col in zipped]
