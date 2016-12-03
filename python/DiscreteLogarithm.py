################## DISCRETE LOGARITHM #######################
##################### May 03, 2016  #########################
#
# https://programmingpraxis.com/2016/05/03/discrete-logarithms/
#
# Your task is to write a program that computes discrete 
# logarithms by trying each possible value in succession 
# until the answer is found. When you are finished, 
# you are welcome to read or run a suggested solution,
# or to post your own solution or discuss the exercise 
# in the comments below.
#
#############################################################

# Power with modulus
# Use the binary representation to build solution quickly
def ppow1(x, y, m):
    x = (x % m)
    currpow = x
    n = 1
    ans = 1
    n = 0 
    while y > 0:
        if y % 2 == 1:
            ans = (ans * currpow) % m
        n += 1
        currpow = (currpow * currpow) % m
        y = y >> 1
    return (ans % m)

# Aha, python has built-in modular pow (specify modulus as third argument
# just as above, so use that instead!
ppow = pow

# Solves for y: x^y = n (mod m)
def sol1(m, x, n):
    n = (n % m)
    y = 1
    while (y < m + 1) and (ppow(x,y,m) != n) :
        y += 1
    if y <= m:
        return y
    return False

def testSol1(m, x, n):
    y = sol1(m, x, n)
    if y is False:
        print x, "^y=", n, 'has no solution mod', m
    else:
        _exp = ppow(x, y, m)
        if (_exp == n %m):
            print x, "^", y, '=', _exp, "=", n, '%', m
        else:
            print "Failed:"
            print x, "^", y, '=', _exp, "!=", n, '%', m

def test_ppow():
    for y in range(0,5):
        print "2^", y, "mod 5 = ", ppow(2, y, 5)
        print ""
    for y in range(0,5):
        print "3^", y, "mod 5 = ", ppow(3, y, 5)
        print ""
    for y in range(0,10):
        print "2^", y, "mod 7", ppow(2, y, 7)
    for y in range(0,10):
        print "3^", y, "mod 7", ppow(3, y, 7)

def test_sol1():
    # Test negative values, and values > m
    for n in range(-10,10):
        testSol1(5, 2, n)
    for n in range(0, 5):
        testSol1(5, 3, n)
    # 2 is not a primitive root mod 7
    # since 2^3 = 1 (mod 7) it has period 3 - (Z/7)* is cyclic of order 6 and 
    # 2^3 is just not a generator of this cyclic group
    # So test for this case
    for n in range(0,7):
        testSol1(7, 2, n)
    for n in range(0,7):
        testSol1(7, 3, n)
    # Also not a generator: 4^3 = 64 = 9*7 + 1
    for n in range(0,7):
        testSol1(7, 4, n)
    for n in range(0,7):
        testSol1(7, 5, n)

if __name__ == '__main__':
    #test_ppow()
    test_sol1()
