# July 22, 2011
#
# The prime-counting function pi(n) computes the number of primes not greater than n,
# and has been a matter of fascination to mathematicians for centuries. The Prime
# Number Theorem tells us that pi(n) is approximately n / log(n); Carl Fredrich
# Gauss proposed the prime number theorem in 1792 when he was only fifteen
# years old, and Jacques Hadamard and Charles-Jean de la Valle Poussin both 
# proved it, independently, in 1896. The first person to make a serious 
# attempt at the calculation, except for trivial attempts that simply enumerated 
# the primes and counted them, was the French mathematician Adrien-Marie 
# Legendre at the end of the eighteenth century; his formula was correct
# , but he erroneously reported that pi(106) = 78526, whereas the correct 
# value is 78498. We will recreate Legendre's calculation in today's exercise.

import sys, os, inspect
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/lib')
import PrimeSieve
from math import sqrt, floor, ceil

class LegendrePrimeCount:
    _memoize = False
    primes = []
    maxprime = 0
    _memoxmax = 1000
    _memoamax = 1000
    _phistore = {}

    def __init__(self, _max):
        # Cheat by precomupting primes up to sqrt(max)
        # How else to get the ath prime?
        intmax = max(10,int(sqrt(float(_max))))
        self.primes = PrimeSieve.primes(intmax)
        self.maxprime = self.primes[len(self.primes)-1]

    # Count all numbers up to x that are not multiples of one of the 
    # first a primes.
    # Note the relation (where pa is the ath prime)
    # phi(x, a) = phi(x, a-1) - phi(int(x/pa), a-1) 
    # phi(x, a) = 0 if pa > x
    # phi(x, 1) =  number of odd numbers less than x
    # Also, should memoize this function
    def _phi(self, x, a):
        if (self._memoize and self.memoized(x,a)):
            return self.memoval(x,a)
        if a == 1:
            return int(floor((x+1)/2))
        pa = self.primes[a-1]
        if (pa >= x):
            return 1
        val = self._phi(x, a-1) - self._phi(int(x/pa), a-1)
        if (self._memoize and x < self._memoxmax and a < self._memoamax):
            self.memoize(x,a,val)
        return val

    def memoized(self, x, a):
        return (self._memoamax*x + a) in self._phistore
    def memoval(self, x, a):
        return self._phistore[self._memoamax*x + a]
    def memoize(self, x, a, val):
        self._phistore[self._memoamax*x + a] = val

    # Primes less than or equal to x
    # Use the fact that
    # pi(x) = phi(x, a) + a - 1, where a = pi(int(sqrt(x)))
    # For small x do a lookup
    # praxis' solution uses a binary search on the existing primes
    def pi(self, x):
        if x < self.maxprime:
            return self._binSearch(x) + 1
        a = self.pi(int(sqrt(float(x))))
        return self._phi(x, a) + a - 1
  
    def _binSearch(self, n):
        if n > self.maxprime:
            raise Exception("Out of range")
        return self._binSearch1(self.primes, n, 0, len(self.primes)-1)
   
    # Return greatest index idx where primes(idx) < n
    def _binSearch1(self, arr, n, lo, hi):
        if (hi < lo):
            return hi
        mid = int((lo + hi)/2)
        if (arr[mid] < n):
            return self._binSearch1(arr, n, mid + 1, hi)
        elif (arr[mid] > n):
            return self._binSearch1(arr, n, lo, mid -1)
        # Found
        return mid
    
def main(args):
    x = 0
    if len(args) < 1:
        x = input('Enter the number you want to compute pi(x) for: ')
    else:
        x = int(args[0])
    pc = LegendrePrimeCount(int(x))
    pc._memoize = True
    cnt = pc.pi(int(x))
    print "Number of primes less than {0:d} is {1:d}".format(x, cnt)

if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)
