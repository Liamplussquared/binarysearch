# https://binarysearch.com/problems/Happy-Numbers
class Solution:
    def solve(self, n):
        encountered = set()

        while True:
            temp = 0
            digits = str(n)
            for digit in digits:
                temp += int(digit) ** 2
            if temp in encountered:
                return False
            elif temp == 1:
                return True
            else:
                encountered.add(temp)
                n = temp
