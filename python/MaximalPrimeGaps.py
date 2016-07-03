import lib.PrimeSieve as PrimeSieve, lib.MillerTest as MillerTest

# Compute all prime gaps
def maximalPrimeGaps(n):
    primes = PrimeSieve.primes(n)
    last = primes[0]
    maxsofar = 0
    result = []
    nprimes = len(primes)
    for i in range(1,nprimes):
        curr = primes[i]
        last = primes[i-1]
        if (curr - last > maxsofar):
            maxsofar = curr - last
        result.append((last,maxsofar))
    return result

# We could compute the sieve and then the gaps
# but there is no need to double the work
def maximalPrimeGapIncreasesViaSieve0(n):
    lst = range(3,n+1)
    primes = [2]
    result = []
    maxsofar = 0
    filter(lambda y: y % 2 != 0, lst)
    lastprime = 2
    while len(lst) > 0:
        x = lst.pop(0)
        diff = x - primes[-1]
        primes.append(x)
        if diff > maxsofar:
            maxsofar = diff
            # I think this is a better answer
            #result.append((x,maxsofar))
            # But this is consistenet with the example
            # given on praxis
            result.append((primes[-2],maxsofar))
        lst = filter(lambda y: y % x != 0, lst)
        if x*x > n:
            break
    return result

# Ahh but that was dumb because we only need to go up to 
# root n in calculating the sieve.  So we're better
# off to compute it first and then loop through the result
def maximalPrimeGapIncreasesViaSieve(n):
    primes = PrimeSieve.primes(n)
    last = primes[0]
    maxsofar = 0
    result = []
    nprimes = len(primes)
    for i in range(1,nprimes):
        curr = primes[i]
        last = primes[i-1]
        if (curr - last > maxsofar):
            maxsofar = curr - last
            result.append((last,maxsofar))
    return result

# For comparison, as above but using Miller
# test instead of Sieve
def maximalPrimeGapIncreases(n):
    i = 3
    result = [(2,1)]
    primes = [2,3]
    maxsofar = 0
    while i <= n:
        i += 2
        if MillerTest.MillerRabin(i):
            last = primes[-1]
            primes.append(i)
            if (maxsofar < i - last):
                maxsofar = i - last
                result.append((last,maxsofar))
    return result

n = input("Enter a number:")
#for x in maximalPrimeGapIncreasesViaSieve(n):
    #print x
#for x in maximalPrimeGapIncreases(n):
    #print x
for x in maximalPrimeGaps(n):
    print x
