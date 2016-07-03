################### Goldbach's Other Conjecture  ######################
######################### June 07, 2016  ##############################
#
# https://programmingpraxis.com/2016/06/07/goldbachs-other-conjecture/
#
# Although it is not as well known, Goldbach made another conjecture 
# as follows: Every odd number greater than two is the sum of 
# a prime number and twice a square; for instance, 
#
# 27 = 19 + 2 * (2 ** 2)
#
# Your task is to write a program that finds the smallest number 
# that disproves Goldbach's other conjecture.
#
#######################################################################

import math, time
import lib.PrimeSieve as PrimeSieve, lib.MillerTest as MillerTest

prime_cache = []
CACHEMAX = 10000

def is_prime(i):
    if (i < CACHEMAX) and i in prime_cache:
        return True
    if MillerTest.MillerRabin(i):
        if i < CACHEMAX:
            prime_cache.append(i)
        return True
    return False


def is_double_square(x):
    y = round(math.sqrt(x/2))
    if abs(2*y*y - x) < 1:
        return True
    return False

def goldbachTest(n):
    x = 3
    while x <= n:
        if is_prime(x):
            y = n - x
            if is_double_square(y):
                return True
        x += 2
    return False

if __name__ == '__main__':
    for i in range(3,99,2):
        print i, goldbachTest(i)
    i = 3
    print 5777, goldbachTest(5777)
    t1 = time.time()
    while goldbachTest(i):
        i += 2
        if ((i % 1000) < 2):
            print "Checked up to", i - 1
    print "Failed on", i
    print "Took ", time.time() - t1, "seconds"
