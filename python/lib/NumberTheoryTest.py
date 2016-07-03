import math,random
import NumberTheory

egcd = NumberTheory.egcd
gcd = NumberTheory.gcd
mod_inverse = NumberTheory.mod_inverse

def test_egcd():
    tests = [ ]
    for i in range(0,10000):
        a , b = random.randint(0,100), random.randint(0,100)
        if random.randint(0,1) == 0:
            a = -a
        if random.randint(0,1) == 0:
            b = -b
        g = abs(gcd(a, b))
        tests.append((a, b, g))
    for (a,b, ed) in tests:
        d, x, y = egcd(a, b)
        if d != ed:
            print "Error on egcd({0:d}, {1:d}):  found gcd = {2:d}, expected {3:d}".format(a, b, d, ed)
            print "Failed ", a, b, ed
            exit(1)
        if (x*a + y*b != d):
            print a, b, ed
            print "Error on egcd: {0:d}*{1:d} + {2:d}*{3:d} = {4:d} != {5:d}".format(a, x, b, y, a*x + b*y, d)
            print "Failed ", a, b, ed
            exit(1)
    print "Passed all tests for egcd"

def test_mod_inverse():
    tests = [ ]
    for i in range(0,10000):
        a , m = random.randint(0,100), random.randint(2,100)
        tests.append((a, m))
    for (a,m) in tests:
        d = gcd(a, m)
        x = mod_inverse(a, m)
        if (d != 1) and (x > 0):
            print "Error - modular inverse should not be found"
            exit(1)
        if (d == 1) and (a*x % m != 1):
            print x, "is not a modular inverse for", a, "(mod ", m, ")"
            exit(1)
    print "Passed all tests for mod_inverse"

if __name__ == '__main__':
    test_egcd()
    test_mod_inverse()
