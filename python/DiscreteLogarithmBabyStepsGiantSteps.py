############### Baby Steps, Giant Steps ####################
#################### May 06, 2016  #########################
#
# https://programmingpraxis.com/2016/05/06/baby-steps-giant-steps/
#
# 1. b = ceil(sqrt(m))
#    h = x^{-b}
# 2. A = {x^i for i in range(0,b)}
#    B = {n*h^j for j in range(0,b)}
# 3. Sort A, B, find the intersection and the indices of i,j in A,B
#
# Then x^i = n * h^j or x^(i + j*b) = n so return i + j*b
#
############################################################

import math

## HELPERS
def index_intersection(A, B):
    i = 0
    j = 0
    while (j < len(B)) and (A[i][1] > B[j][1]):
        j += 1
    while (i < len(A)) and (j < len(B)) and (A[i][1] < B[j][1]):
        i += 1
        while (i < len(A)) and (j < len(B)) and (A[i][1] > B[j][1]):
            j += 1
    if (i >= len(A)) or (j >= len(B)):
        return False, False
    if A[i][1] == B[j][1]:
        return i, j
    else:
        return False, False

def mod_inverse(x, m):
    # We do know that x^(m-1) = 1 because (Z/m)* is cyclic of order (m-1)
    # So x^{-1} = x^{-m} = x^{-m + (m-1) + (m-1)} = x^{m-2}
    # Or simply bc x^{m-2} * x = x^{m-1} = 1
    return pow(x, m-2, m)

def sol1(m, x, n):
    n = (n % m)
    b = int(math.ceil(math.sqrt(m))) + 1
    h = mod_inverse(x, m)
    h = pow(h,b,m)

    A = [ [i, (pow(x,i,m) % m) ] for i in range(0,b)]
    B = [ [j, (n * pow(h,j,m)) % m ] for j in range(0,b)]

    A.sort(lambda x, y: -1 if x[1] < y[1] else 1)
    B.sort(lambda x, y: -1 if x[1] < y[1] else 1)

    #print A, B
    i,j = index_intersection(A,B)
    if (i is False) or (j is False):
        return False

    # ans is an exponent, so take it mod (m-1) since (m-1) is the
    # order of the multiplicative group
    ans = (A[i][0] + b*B[j][0]) % (m-1)
    return ans

# Testing
def test_mod_inverse():
    for i in range(1,6):
        j = mod_inverse(i, 7)
        print i, j, ((i*j) % 7)

def test_index_intersection():
    print "Should have solution, 2 is in both lists"
    A = [[0,1],[1,2],[2,3]]
    B = [[0,2],[1,3],[2,4]]
    i,j = index_intersection(A, B)
    if A[i][1] != B[j][1]:
        print "FAIL"
    print i, j, A[i][1], "=", B[j][1]
    i,j = index_intersection(B, A)
    print i, j, A[j][1], "=", B[i][1]

    print "Should have solution, 2 is in both lists"
    A = [[0,2],[1,3],[2,4]]
    B = [[0,1],[1,2],[2,3]]
    i,j = index_intersection(A, B)
    if A[i][1] != B[j][1]:
        print "FAIL"
    print i, j, A[i][1], "=", B[j][1]
    i,j = index_intersection(B, A)
    print i, j, A[j][1], "=", B[i][1]

    print "Should have no solution"
    A = [[0,1],[1,2],[2,3]]
    B = [[0,4],[1,5],[2,6]]
    i,j = index_intersection(A, B)
    if i is not False:
        print "FAIL"
    print i, j, A[i][1], "=", B[j][1]
    i,j = index_intersection(B, A)
    print i, j, A[j][1], "=", B[i][1]

    print "Should have solution, 5 is in both lists"
    A = [[0,1],[1,2],[2,3],[3,5],[4,9]]
    B = [[0,4],[1,5],[2,6]]
    i,j = index_intersection(A, B)
    if A[i][1] != B[j][1]:
        print "FAIL"
    print i, j, A[i][1], "=", B[j][1]
    i,j = index_intersection(B, A)
    print i, j, A[j][1], "=", B[i][1]

    print "Both lists contain 1,2,4"
    A = [[0, 1], [3, 1], [1, 2], [2, 4]]
    B = [[2, 1], [1, 2], [0, 4], [3, 4]]
    i,j = index_intersection(A, B)
    if A[i][1] != B[j][1]:
        print "FAIL"
    print i, j, A[i][1], "=", B[j][1]
    i,j = index_intersection(B, A)
    print i, j, A[j][1], "=", B[i][1]


def modulus_test_sol1(m, x):
    for n in range(2,m):
        ans = sol1(m, x, n)
        if ans is not False:
            _exp = pow(x, ans, m)
            passed = (_exp == n %m)
            if passed:
                return True
            else:
                print "Failed to calculate log of ", n, "to base",x, "in modulus", m
                return False
        else:
            for j in range(0,m):
                _exp = pow(x, j, m)
                if _exp == n:
                    return False
            return True
            
def full_modulus_test(m):
    passed = True
    for x in range(2,m):
        if not modulus_test_sol1(m, x):
            print "Failed modulus m", m, " on base ", x
            passed = False
    return passed
        
def test_sol1():
    ps = [2,3,5,7,11,13,17,19,101,113,1009]
    passed = True
    for p in ps:
        if not full_modulus_test(p):
            passed = False
    if passed:
        print "Passed all tests"

if __name__ == '__main__':
    #test_index_intersection()
    print "Testing logarithm method"
    test_sol1()
