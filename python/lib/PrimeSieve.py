import sys

def primes(n):
    lst = range(2,n+1)
    primes = []
    while len(lst) > 0:
        x = lst.pop(0)
        primes.append(x)
        lst = filter(lambda y: y % x != 0, lst)
        if x*x > n:
            break
    return primes + lst
