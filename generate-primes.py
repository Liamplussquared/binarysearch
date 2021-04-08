# https://binarysearch.com/problems/Generate-Primes
class Solution:
    def solve(self, n):
        # using Sieve of Eratosthenes
        if n < 2:
            return []
        elif n == 2:
            return [2]

        A = [True] * (n+1)
        res = []

        for i in range(2, int(sqrt(n))+1):
            if A[i]:
                for j in range(i*i, n+1, i):
                    A[j] = False

        for i in range(2, n+1):
            if A[i]:
                res.append(i)

        return res                
        
        