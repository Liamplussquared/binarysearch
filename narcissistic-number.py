# https://binarysearch.com/problems/Narcissistic-Number
def narcissistic_number(n):
    num_digits = len(str(n))
    res = 0
    original_n = n

    while n:
        res += (n % 10) ** num_digits
        n //= 10

    return original_n == res
    