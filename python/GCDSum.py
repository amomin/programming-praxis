######################### GCD SUM #############################
##################### April 22, 2016  #########################
#
# Today's exercise is inspired by A018804: Find the sum of 
# the greatest common divisors gcd(k, n) for 1 <= k <= n.
#
##############################################################

def gcd(a, b):
    def _gcd(sm, lrg):
        if sm == 0:
            return lrg
        return _gcd(lrg % sm, sm)
    mn = min(a,b)
    mx = max(a,b)
    return _gcd(mn, mx)


# Solution should be approx O(n log n)
# Can make it twice as fast using gcd(k,n) = gcd(k-n,n)
# but we won't
def sol1(n):
    sum = 0
    for k in range(0,n):
        sum += gcd(k, n)
    return sum

if __name__ == '__main__':
    for n in range(0,20):
        print "f(", n, ") = ",  sol1(n)

############## After read more ##############

# Functional style
def sol2(n):
    return sum ( map( lambda x: gcd(x, n), range(0,n) ) )

if __name__ == '__main__':
    for n in range(0,20):
        print "f(", n, ") = ",  sol2(n)

# The site claims that using a strategy to consider by factors instead -
# i.e. group the sum by elements having the same gcd d, which is easy to figure
# out because there are phi(n/d) many such k - is much faster.
# You need to have implementations of phi and/or finding divisors of n.
#def sol3(n):
#    sum = 0
#    for d in divisors(n):
#      sum += d * phi(n/d)
#    return sum
