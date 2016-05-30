#!/usr/bin/python
############### Baby Steps, Giant Steps ####################
#################### May 06, 2016  #########################
#
# https://programmingpraxis.com/2016/05/27/pollards-rho-algorithm-for-discrete-logarithms
#
# I think something isn't quite right with this algorithm....
#
############################################################

import math

def my_gcd(a, b):
    if a < 0:
        return my_gcd(a + abs(a)*b, b)
    if b < 0:
        print "HELP ITS NEG"
    def _gcd(sm, lrg):
        if sm == 0:
            return lrg
        return _gcd(lrg % sm, sm)
    mn = min(a,b)
    mx = max(a,b)
    return _gcd(mn, mx)

def _check_loop_invariant(x,a,b,p,t,g):
    if ( (x % p) != (pow(t,a,p) * pow(g,b,p) % p) ):
        print "Loop invariant failed"
        print x % p, "mod", p
        print pow(t,a,p) * pow(g,b,p) % p, "mod", p
        return False
    return True

def _nextIterate(x1,a1,b1,p,t,g):
    x2,a2,b2 = 0,0,0
    if not _check_loop_invariant(x1,a1,b1, p, t, g):
        print "Initial Check Failed"
    if (3*x1 < p):
        a2 = (a1+1) % (p - 1)
        b2 = b1 % (p - 1)
        x2 = (t*x1) % p
    elif (p < 3*x1) and (3*x1 < 2*p):
        a2 = 2*a1 % (p - 1)
        b2 = 2*b1 % (p - 1)
        x2 = (x1*x1) % p
    #elif (2*p < 3*x1) and (x1 < p):
    else:
        a2 = a1 % (p - 1)
        b2 = (b1+1) % (p - 1)
        x2 = (g*x1) % p
    if not _check_loop_invariant(x2,a2,b2, p, t, g):
        print "Final Check Failed"
    return x2,a2,b2

# Note m might not be prime
# We do a stupid solution just for now
def mod_inverse(x, m):
    i = 0
    x = x % m
    while i < m:
        if (x*i % m) == 1:
            return i
        i += 1
    print "NO SOLUTION TO MOD PROBLEM"
    exit(1)

# Solve a*x = b mod m
# Do a stupid solution for now
def solve_lin_congruence(a, b, m):
    a = a % m
    b = b % m
    ans = 0
    while ( (a*ans % m) != (b % m) ) and ans < m:
        ans += 1
    if ((a * ans) % m) != (b % m):
        message = "SOLVE ERROR SOLVING CONGRUENCE" + str(a) + "*" + str(ans) + "=" + \
            str(a*ans) + "!=" + str(b) + "mod" + str(m)
        raise Exception(message)
    return ans

def sol1(p,g,t, debug = False):
    x1, a1, b1 = 1, 0, 0
    x2, a2, b2 = _nextIterate(x1,a1,b1,p,t,g)
    # Loop invariants: x1 = t^a1 * g ^ b1
    # Loop invariants: x2 = t^a2 * g ^ b2
    while x1 != x2:
        if debug:
            print [x1,a1,b1],[x2,a2,b2]
        x1, a1, b1 = _nextIterate(x1, a1, b1, p, t, g)
        x2, a2, b2 = _nextIterate(x2, a2, b2, p, t, g)
        x2, a2, b2 = _nextIterate(x2, a2, b2, p, t, g)
    d = my_gcd(a1 - a2, p - 1)
    if debug:
        print d, [x1,a1,b1],[x2,a2,b2]
    l = 0
    if d == 1:
        try:
            l = solve_lin_congruence(a1 - a2, b2 - b1, p-1)
        except Exception as ex:
            print ex.message
            return False
        else:
            if not ((pow(g, l, p) % p) == t):
                message = "ERROR" + str(g) + "^" + str(l) + "=" + \
                    str(pow(g, l, p)) + "!==" +  str(t) + "mod" + str(p)
                raise Exception(message)
        return l
    else:
        try:
            m = (p-1)/d
            a = (a1-a2) % m
            b = (b2 - b1) % m
            if debug:
                print "Solve:", a, "*x =", b, "mod", m
            l0 = solve_lin_congruence(a, b, m)
        except Exception as ex:
            if debug:
                print "Exception caught: ", ex.message
            return False
        else:
            # Check solution
            if (a *l0 % m) != b:
                print "Not a solution?"
            else:
                if debug:
                    print "SOLUTION ", l0, ":", (a*l0 % m), b
            m1 = 0
            while m1 < d:
                l = l0 + m1*m
                if debug:
                    print m1, l
                if ((pow(g, l, p) % p) == t):
                    return l
                m1 += 1
    return False

### THIS SOLUTION IS FROM PROGRAMMING PRAXIS
from fractions import gcd
def inverse(x, m):
    a, b, u = 0, m, 1
    while x > 0:
        x, a, b, u = b % x, u, x, a - b // x * u
    if b == 1: return a % m
    return 0 # must be coprime
def praxis_dlog(g,t,p):
    # l such that g**l == t (mod p), with p prime
    # algorithm due to Crandall/Pomerance "Prime Numbers" sec 5.2.2
    def f(xab):
        x, a, b = xab[0], xab[1], xab[2]
        if x < p/3:
            return [(t*x)%p, (a+1)%(p-1), b]
        if 2*p/3 < x:
            return [(g*x)%p, a, (b+1)%(p-1)]
        return [(x*x)%p, (2*a)%(p-1), (2*b)%(p-1)]
    i, j, k = 1, [1,0,0], f([1,0,0])
    while j[0] <> k[0]:
        print i, j, k
        i, j, k = i+1, f(j), f(f(k))
    print i, j, k
    d = gcd(j[1] - k[1], p - 1)
    if d == 1: return ((k[2]-j[2])%(p-1) * inverse((j[1]-k[1])%(p-1),p-1)) % (p-1)
    m, l = 0, ((k[2]-j[2])%((p-1)/d) * inverse((j[1]-k[1])%((p-1)/d),(p-1)/d)) % ((p-1)/d)
    while m <= d:
        print m, l
        if pow(g,l,p) == t: return l
        m, l = m+1, (l+((p-1)/d))%(p-1)
    return False
### END OF THIS SOLUTION IS FROM PROGRAMMING PRAXIS

### TESTING PRAXIS SOLUTION ###
def  modulus_test_praxis(m, x):
    for n in range(2,m):
        #ans = sol1(m, x, n)
        ans = praxis_dlog(x, n, m)
        if ans is not False:
            _exp = pow(x, ans, m)
            passed = (_exp == n %m)
            if not passed:
                print "Failed to calculate log of ", n, "to base",x, "in modulus", m
                return False
        else:
            for j in range(2,m):
                _exp = pow(x, j, m)
                if _exp == n:
                    print "Found unexpected solution", x, "^", j, "=", _exp, "=", n, "mod", m
                    return False
    return True
def full_modulus_test_praxis(m):
    passed = True
    for x in range(2,m):
        if not modulus_test_sol1(m, x):
            print "Failed modulus m", m, " on base ", x
            passed = False
        else:
            print "Passed modulus m", m, " on base ", x
    return passed
def test_praxis():
    ps = [13]
    passed = True
    for p in ps:
        if not full_modulus_test_praxis(p):
            passed = False
    if passed:
        print "Passed all tests"
### TESTING PRAXIS SOLUTION ###

def  modulus_test_sol1(m, x):
    for n in range(2,m):
        ans = sol1(m, x, n)
        if ans is not False:
            _exp = pow(x, ans, m)
            passed = (_exp == n %m)
            if not passed:
                print "Failed to calculate log of ", n, "to base",x, "in modulus", m
                return False
        else:
            for j in range(2,m):
                _exp = pow(x, j, m)
                if _exp == n:
                    print "Found unexpected solution", x, "^", j, "=", _exp, "=", n, "mod", m
                    return False
    return True
            
def full_modulus_test(m):
    passed = True
    for x in range(2,m):
        if not modulus_test_sol1(m, x):
            print "Failed modulus m", m, " on base ", x
            passed = False
        else:
            print "Passed modulus m", m, " on base ", x
    return passed

def test_solve_lin_congruence():
    try:
        ans = solve_lin_congruence(2, 7, 12)
    except Exception as ex:
        ans = 0
    else:
        print "ERROR - should have caught exception"

    if ans:
        print "Error - no solution to this congruence"
    ans = solve_lin_congruence(2, 6, 12)
    if ans != 3:
        print "Failed to solve 2x = 6 mod 12"
    primes = [5,7,11,13,101]
    for p in primes:
        for real_ans in range(0,p-1):
            for a in range(1,p-1):
                ans = solve_lin_congruence(a, a*real_ans, p)
                if ans != real_ans:
                    print "Failed to solve ", a, "*x = ", real_ans, \
                        "mod", p, " - got", ans

def test_sol1():
    #ps = [2,3,5,7,11,13,17,19,101,113,1009]
    ps = [13]
    passed = True
    for p in ps:
        if not full_modulus_test(p):
            passed = False
    if passed:
        print "Passed all tests"

if __name__ == '__main__':
    #test_solve_lin_congruence()
    #print sol1(997,83,555, True)
    #print sol1(997,83,566, True)
    print "TESTING IMPLEMENTED SOLUTION:"
    test_sol1()
    print "TESTING PROVIDED SOLUTION:"
    test_praxis()
