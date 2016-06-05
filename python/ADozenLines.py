################## A Dozen Lines of Code ######################
###################### June 03, 2016  #########################
#
# Your task is to write some interesting and useful program
# in no more than a dozen lines of code.
#
###############################################################

# We implement a few solutions here: quicksort,
# prime testing, prime listing, exponentiation in finite cyclic group
#
# None of these are optimal but each is pretty concise and
# does something useful
#
# FWIW praxis implemented hash tables - but kinda cheated wrt the
# whole 12 lines thing ;)

import math

# Quicksort
def sol1(arr):
    if len(arr) < 2:
        return arr
    else:
        piv = arr[0]
        is_eq = lambda x: x == piv
        is_less = lambda x: x < piv
        is_more = lambda x: x > piv
        return sol1(filter(is_less, arr)) + \
            filter(is_eq, arr) + \
            sol1(filter(is_more, arr))

# Is Prime
def sol2(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

# List of primes up to n, via Sieve of Eratothsenes
def sol3(n):
    res = range(2,n + 1)
    if n < 20:
        return filter(lambda x: x <= n, [2,3,5,7,11,13,17])
    ps_up_to_sqrt = sol3(int(math.sqrt(n)))
    for i in ps_up_to_sqrt:
        res = filter(lambda x: (x == i) or (x % i != 0), res)
    return res

# "Fast" Modular power raising - should be identical to pow(b, e, m)
# on "admissible" input
def sol4(b, e, m):
    if e < 0: raise Exception("Require positive exponent")
    if b < 1: raise Exception("Require base > 0")
    if m < 2: raise Exception("Require modulus > 1")
    ans = 1
    curr = b
    while e > 0:
        if e % 2 != 0:
            ans = (ans * curr) % m
        curr =  (curr * curr) % m
        e = e >> 1
    return ans

import random

if __name__ == '__main__':
    print "Demo quicksort"
    unsorted = []
    for i in range(0,10):
        unsorted.append(random.randint(0,100))
    print unsorted, sol1(unsorted)
    
    print "Demo \"Is Prime\": from 100 to 140"
    print filter(sol2, range(100,141))

    print "Demo Sieve of Eratothsenes (up to 50)"
    print sol3(50)

    print "Demo mod power raising"
    #print sol4(2,-1,13)
    #print sol4(0,1,13)
    #print sol4(2,3,1)
    for i in range(0,12):
        ans1 = sol4(2, i, 13)
        ans2 = pow(2, i, 13)
        print 2, i, 13, ans1, ans2
