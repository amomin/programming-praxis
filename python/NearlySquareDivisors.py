###################### Nearly-Square Divisors ##########################
##################### August 05, 2016  #########################
#
# Given positive integers n, a and b such that n = a * b with a >= b,
# find a and b such that the difference a - b is as small as possible.
#
# Your task is to write a program to find a and b as described
# above; use your program to find the nearly square divisors
# of n = 224403121196654400.
#
##############################################################

from lib.NumberTheory import factor
from math import sqrt

def max_divisor_less_or_equal_sqrt(n):
    factors = factor(n)
    max_factor = sqrt(n)
    divisors = [1]
    for [p, k] in factors:
        addon = []
        for i in range(1,k+1):
            addon += map(lambda(x) : x * (p**i), divisors)
        divisors += addon
        divisors = filter(lambda(x) : x <= max_factor, divisors)
    divisors = sorted(divisors)
    max_divisor = divisors[len(divisors) - 1]
    return max_divisor

def difference(n):
    max_divisor = max_divisor_less_or_equal_sqrt(n)
    return (n / max_divisor) - max_divisor

if __name__ == '__main__':
    print 6, max_divisor_less_or_equal_sqrt(6), difference(6)
    print 36, max_divisor_less_or_equal_sqrt(36), difference(36)
    print 72, max_divisor_less_or_equal_sqrt(72), difference(72)
    print 224403121196654400, max_divisor_less_or_equal_sqrt(224403121196654400), difference(224403121196654400)

