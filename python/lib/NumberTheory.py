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
	return gcdminmax(m,n)

def gcdminmax(a,b):
	if (b%a) == 0:
		return a
	else:
		return gcdminmax(b%a,a)

# Returns a list of prime factors of n with the power of the exponent
# e.g. factor(12) = [[2,2],[3,1]]
def factor(n):
	f=2
	_max = n/2 + 1
	_factors=[]
	while n>1 and f< _max:
		k=0
		while (n%f==0):
			k+=1
			n/=f
		if k>0:
			_factors.append([f,k])
		f+=1
		_max = int(math.sqrt(n))+1
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

