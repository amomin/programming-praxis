###################### Binary Search ##########################
##################### April 29, 2016  #########################
#
# Your task is to write a binary search function; do it 
# yourself, without looking at any library implementations 
# or searching the internet.
#
##############################################################

def bin_search1(lst, x):
    return _bin_search1(lst, x, 0, len(lst))

# Invariants:
# lst is sorted
# If x is in lst, its index is at least lo
# If x is in lst, its index is less than hi
def _bin_search1(lst, x, lo, hi):
    if (lo >= hi):
        # can't be at least lo and less than hi
        # if lo >= hi
        return False
    # mid is at least lo, and at most hi
    mid = (lo + hi) / 2
    if lst[mid] == x:
        return mid
    elif lst[mid] < x:
        # If x is in the list, its index at least mid + 1
        return _bin_search1(lst, x, mid + 1, hi)
    else: # x < lst[mid]
        # If x is in the list, its index less than mid
        return _bin_search1(lst, x, lo, mid)

def test(lst, x, expected):
    res = bin_search1(lst, x)
    #print "Testing:", lst, x, 'Expecting:', expected, "Got:", res
    #print "Passed?", expected == res
    return expected == res

def testconsistent(lst, x, notinlist):
    res = bin_search1(lst, x)
    passed = False
    if (res == False) and notinlist:
        passed = True
    elif (res == False) and (res != 0):
        print "Wasn't found but should have been",lst,x,res
        passed = False
    else:
        passed = lst[res] == x
        if not passed:
            print "Found the wrong index"
    return passed

if __name__ == '__main__':
    test([1], 1, 0)
    test([1], 2, False)
    test([1], -1, False)
    test([1,2], 1, 0)
    test([1,2], 2, 1)
    test([1,2], 3, False)

    numpass = 0
    numfail = 0
    print "Running tests"
    for n in range(3,10):
        lst = map(lambda x: 2*x + 1, range(0,n))
        for k in range(0,2*n + 1):
            expected = False
            if k % 2 == 1:
                expected = k/2
            passed = test(lst, k, expected)
            if not passed:
                numfail += 1
            else:
                numpass += 1
    print "Tests complete, passed", numpass, "failed", numfail

    # What if repeats in list?
    testconsistent([1,2,2],1, False)
    testconsistent([1,2,2],2, False)
    testconsistent([1,2,2],0, True)
    testconsistent([1,2,2],3, True)
    testconsistent([1,1,2],1, False)
    testconsistent([1,1,2],2, False)
    testconsistent([1,1,2],0, True)
    testconsistent([1,1,2],3, True)
    testconsistent([1,1,1],1, False)
    testconsistent([1,1,1],2, True)
    testconsistent([1,1,1],0, True)
    testconsistent([1,1,1],3, True)
