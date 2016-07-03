import math

def phi(m): # Returns the value of Euler's Totient function phi(n)
    i = 2
    answer = 1
    while i*i <= m:
        k = 0
        while (m%i) == 0: #i divides m, count how many times
            k+=1
            m/=i
        if k > 0:
            answer *= (i**(k-1))*(i-1) #totient function is multiplicative, and equal to p^(k-1)(p-1) if m = p**(k)
        i+=1
    if m>1:
        return answer*(m-1)
    else:
        return answer

def gcd(a,b):
    m = min(a,b)
    n = max(a,b)
    if m == 0: return n
    return gcdminmax(m,n)

def gcdminmax(a,b):
    if (b%a) == 0: return a
    else: return gcdminmax(b%a,a)

# egcd(a, b):
#
# Given:   integers a, b
# Returns: integers d, x, y such that d = x*a + y*b
#
# This can be used in several ways: to calculate the gcd, but also to calculage
# a modular inverse of b (mod a) when (a, b) = 1, since:
#
# 1 = y*b = (x*a + y*b) (mod a) 
#
# Explanation: Without loss of generality suppose a > b > 0 and let r0 = a, r1 = b
# We can produce the sequence of remainders r0 > r1 > r2 > ... > rn > r(n+1) = 0
# as r(i+2) = r(i) - qi * r(i+1)
# However we get more information if we keep track of the vector Ri = [ri; r(i+1)]
# which are determined by matrix multiplication as follows:
# R(i+1) = M(i) * Ri, where M(i) = [0,1;1,-qi]
#
# We seek R(n) = [d; 0]
# R(n) = P * R(0), where P = M(n-1)*M(n-2)*....*M(0)
#
# If P = [x,y;w,z], notice that the top row of this product yields
#
# d = x*a + y*b
#
# We compute the entries of the partial products P(i) = M(i) * ... * M(0)
# with entries P(i) = [xi,yi;wi,zi] - using P(i+1) = M(i+1) * P(i) - as
#
# x(i+1) = wi
# y(i+1) = zi
# w(i+1) = xi - q(i+1)*wi
# z(i+1) = yi - q(i+1)*zi
#
# After these observations the algorithm to produce d, x, y is evident.
def egcd(a, b):
    pa, pb, sa, sb = abs(a), abs(b), 1 if a > 0 else -1, 1 if b > 0 else -1
    ord = True if pa > pb else False
    m, n = max(pa, pb), min(pa, pb)
    r0, r1 = m, n
    x,y,w,z = 1,0,0,1
    while r1 > 0:
        q = r0 / r1
        r0, r1 = r1, r0 - q*r1
        x, y, w, z = w, z, x - q*w, y - q*z
    # Sanity check - this should now be true
    #if x*m + y*n != r0:
        #raise Exception("Wrong ax + by != r0", x*m + y*n, r0)
    if ord:
        # Then pa > pb so
        # x * pa + y * pb = d
        # (sa*x)*a + (sb*y)*b = d
        ans = r0, sa * x, sb * y
    else:
        # Then pb > pa so
        # x * pb + y * pa = d
        # (sb * x) * b + (sa * y) * a = d
        # (sa * y) * a + (sb * x) * b = d
        ans = r0, sa * y, sb * x
    return ans

# mod_inverse(a, b)
#
# Given:   integers a, m
# Returns: If a, m are coprime, returns an integer x such that x*a = 1 (mod m)
#          If not, return 0
#
# Expect:  m should be at least 2
#
# Uses egcd to compute:
# d = a*x + m*y so d = a*x (mod m)
# If d == 1, then we have an inverse.
# Else a, m are not coprime, no modular inverse for a exists (mod m)
def mod_inverse(a, m):
    if m < 2: return 0
    d, x, y = egcd(a, m)
    if d == 1: return x
    else: return 0

# Returns a list of prime factors of n with the power of the exponent
# e.g. factor(12) = [[2,2],[3,1]]
def factor(n):
    f=2
    #_max = n/2 + 1
    _max = int(math.sqrt(n))+1
    _factors=[]
    while n>1 and f< _max:
        k=0
        while (n%f==0):
            k+=1
            n/=f
        if k>0:
            _factors.append([f,k])
            _max = int(math.sqrt(n))+1
        f+=1
        #_max = int(math.sqrt(n))+1
    if n > 1:
        _factors.append([n,1])
    return _factors

def sumProperDivisors(n):
    x = factor(n)
    result = 1
    for [p,k] in x:
        result *= (p**(k+1)-1)/(p-1)
    if result==n:
        return result
    return result - n # Remove the term 'n'

