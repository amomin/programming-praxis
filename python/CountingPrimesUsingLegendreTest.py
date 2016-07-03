import CountingPrimesUsingLegendre

def binSearchTest():
    tests = [4000,4500,5000]
    values = [(1,-1), (2, 0), (3, 1), (4, 1), (11, 4), (22, 7)]
    _pass = True
    for x in tests:
        x = 1000
        pc = CountingPrimesUsingLegendre.LegendrePrimeCount(int(x))
        for (t,v) in values:
            val = pc._binSearch(t)
            if val != v:
                print "Failed on search for {0:d} = {1:d}, got {2:d}".format(t, v, val)
                _pass = False
    return _pass

def piTest():
    values = [(1,0),(2,1),(3,2),(4,2),(5,3),(20,8),(25,9),(1000000,78498)]
    _pass = True
    for (t,v) in values:
        pc = CountingPrimesUsingLegendre.LegendrePrimeCount(t)
        cnt = pc.pi(t)
        if cnt != v:
            print "Failed on pi({0:d}) = {1:d}, got {2:d}".format(t, v, cnt)
            _pass = False
    return _pass

def phiTest():
    values = [(10,1,5),(21,1,11),(10,2,3),(50,3,14)]
    _pass = True
    for (x,a,v) in values:
        pc = CountingPrimesUsingLegendre.LegendrePrimeCount(x)
        phival = pc._phi(x,a)
        if phival != v:
            print "Failed on phi({0:d},{1:d}) = {2:d}, got {3:d}".format(x, a,
                v, phival)
            _pass = False
    return _pass

def memoTest():
    values = [10,100,1000,10000,1000000,10000000]
    _pass = True
    for x in values:
        pc1 = CountingPrimesUsingLegendre.LegendrePrimeCount(x)
        pc1._memoize = True
        pc2 = CountingPrimesUsingLegendre.LegendrePrimeCount(x)
        pc2._memoize = False
        pi1 = pc1.pi(x)
        pi2 = pc2.pi(x)
        if pi1 != pi2:
            print "Failed on {0:d}: {1:d} != {2:d}".format(x, pi1, pi2)
            _pass = False
    return _pass

if __name__ == "__main__":
    if binSearchTest():
        print "binSearchTest passed"
    else:
        print "binSearchTest failed"
    if piTest():
        print "piTest passed"
    else:
        print "piTest failed"
    if phiTest():
        print "phiTest passed"
    else:
        print "phiTest failed"
    if memoTest():
        print "memoTest passed"
    else:
        print "memoTest failed"
