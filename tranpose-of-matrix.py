# https://binarysearch.com/problems/Transpose-of-a-Matrix
class Solution:
    def solve(self, matrix):
        n = len(matrix)
        tranpose = [[0 for i in range(n)] for j in range(n)]

        for i in range(n):
            for j in range(n):
                tranpose[i][j] = matrix[j][i]

        return tranpose
