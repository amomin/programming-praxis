import math

# Returns a list of prime factors of n
# e.g. factor(12) = [2,3]
def factors(n):
	f=2
	_max = n/2 + 1
	_factors=[]
	while n>1 and f< _max:
		k=0
		while (n%f==0):
			k+=1
			n/=f
		if k>0:
			_factors.append(f)
		f+=1
		_max = int(math.sqrt(n))+1
	if n > 1:
		_factors.append(n)
	return _factors

def countDiff(list1, list2):
     return len(filter((lambda x : not (x in list1)), list2) + filter (lambda x: not(x in list2),list1))

def dumbSolution(n,m):
    return 0 == countDiff(factors(n),factors(m))

## Smarter solution using gcd
# Using the gcd occurred to me at first, but cases like
# 8*9*5 and 2*9*125 threw me off because you can't just divide
# out by the gcd
# But you can divide it out, then compute the remaining common factors, divide
# those out, etc... until there is nothing left to divide out (i.e. g = 1)
# If there are any factors left over then there was some prime that divides
# n but not the gcd of n and m
# Clearly this will be much faster because we are using gcd (Euclid's algorithm i.e.
# O(log(n))) rather than factoring the number which can be painfully slow i.e.
# O(sqrt(n)) as implemented at least
def smartSolution(n,m):
    def gcd(a,b):
        def gcdminmax(a,b):
            if (b%a) == 0:
                return a
            else:
                return gcdminmax(b%a,a)
        m = min(a,b)
        n = max(a,b)
        return gcdminmax(m,n)

    # Reduces by factoring out all factors of g out of x
    def red(x,g):
        if g == 1: return x
        y = x / g
        gg = gcd(y,g)
        return red(y, gg)

    g = gcd(n,m)
    return (1 == red(n,g)) and (1 == red(m,g))

n = input('Enter a number')
m = input('Enter another number')
nps = factors(n)
mps = factors(m)
print "Prime factors of ", n, " are ", nps
print "Prime factors of ", m, " are ", mps

print "Answer is ", dumbSolution(n,m)
print "Answer is ", smartSolution(n,m)
print "Size of difference set is ", countDiff(nps,mps)
