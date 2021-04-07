# https://binarysearch.com/problems/Ugly-Number
class Solution:
    def solve(self, n):
        if n == 0:
            return False
        if n < 3:
            return True

        factors = []
        while n % 2 == 0:
            n //= 2

        for i in range(3, int(sqrt(n))+1, 2):
            while n % i == 0:
                factors.append(i)
                n //= i

        if n > 2: 
            factors.append(n)
        print(factors)
        for factor in factors:
            if factor != 2 and factor != 3 and factor != 5:
                return False

        return True
            
        