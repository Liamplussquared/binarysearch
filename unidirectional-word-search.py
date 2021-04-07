# https://binarysearch.com/problems/Unidirectional-Word-Search
# messy O(n^2) solution
class Solution:
    def solve(self, board, word):
        n, m = len(board), len(board[0])
        k = len(word)

        if k > n and k > m:
            return False

        # checks rows 
        for row in board:
            res = ""
            for i in range(len(row)):
                res += row[i]
            if word in res:
                return True

        # check columns 
        columns = list(zip(*board))
        for column in columns:
            res = ""
            for i in range(len(column)):
                res += column[i]
            if word in res:
                return True

        return False