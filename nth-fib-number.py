# https://binarysearch.com/problems/Nth-Fibonacci-Number
class Solution:
    def solve(self, n):
        if n > 0 and n < 3:
            return 1

        fib = [1, 1]
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])

        return fib[n - 1]
