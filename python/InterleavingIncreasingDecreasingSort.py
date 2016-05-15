######### Interleaved Increasing-Decreasing Sort  #############
##################### May 13, 2016  #########################
#
# https://programmingpraxis.com/2016/05/13/interleaved-increasing-decreasing-sort/
#
# This must be somebody's homework:
#
# Given an array of integers, rearrange the elements of the array 
# so that elements in even-indexed positions are in ascending 
# order and elements in odd-indexed positions are in descending 
# order. For instance, given the input 0123456789, the desired 
# output is 0927456381, with the even-indexed positions in ascending
# order 02468 and the odd-indexed positions in descending order 
# 97531.
#
##############################################################

# Interleaves two arrays if of the right size (that is,
# an element of B can be fit between every two elements of A and
# an element of A can be fit between every two elements of B)
def _interleave(A,B):
    if (len(A) > len(B) + 2) or (len(B) > len(A)):
        raise Exception("Matrices cannot be interleaved due to size")
    return [A[j/2] if (j % 2 == 0) else B[j/2] for j in range(0,len(A) + len(B))]

# Not in place, so uses (at least) twice the necessary space, but
# uses the internal sort function
def idsort1(arr):
    A = [arr[2*j] for j in range(0,(len(arr)+1)/2)]
    B = [arr[2*j+1] for j in range(0,(len(arr))/2)]
    A.sort()
    B.sort(lambda x, y: -1 if x > y else 1)
    return _interleave(A,B)

# Praxis' solution: sort, then reverse the odd indices.  (Almost) in place
# if the built-in sort is inplace, which it probably is (assuming it uses
# quicksort).
#
# Except... I'm not sure this actually works - see the test on input
# A = [1,5,2,3]
# OK this satisfies the constraints of the problem stated, but does not satisfy 
# the additional constraint (again, not part of the problem but may be
# a desired property) that the odd and even elements remain odd/even elements 
# after re-arrangement.
def idsort2(arr):
    arr.sort()
    i1 = 1
    i2 = len(arr) - 1 if (len(arr) % 2 == 0) else len(arr) - 2
    while i1 < i2:
        tmp = arr[i1]
        arr[i1] = arr[i2]
        arr[i2] = tmp
        i1 += 2
        i2 -= 2
    return arr

# Test if an array is idsorted
def is_idsorted(arr):
    for i in range(0,len(arr) - 2):
        if i % 2 == 0:
            if arr[i] > arr[i+2]:
                return False
        else:
            if arr[i] < arr[i+2]:
                return False
    return True

# Test the helper interleave function
def test_interleave():
    print _interleave([1,2,3],[4,5])
    print _interleave([1,2,3],[4,5,6])
    # Raises Exception
    print _interleave([1,2],[3,4,5])

# Test the interleave method
def _test_idsort1_matrix(method, A):
    arr = method(A)
    if not is_idsorted(arr):
        print "Fail: ", A, method(A)

def _test_idsort1_expected(method, A, expected):
    arr = method(A)
    fail = False
    if len(A) != len(arr):
        print "Failed, length of result does not match input"
        print A, arr, expected
        return False
    for i in range(0, len(A)):
        if arr[i] != expected[i]:
            #print "FAIL AT POS", i, arr[i], expected[i]
            fail = True
    if fail:
        print "Failed while checking that", arr, "equals", expected

def test_idsort():
    fails = 0
    A = [1,2]
    _test_idsort1_expected(idsort1, A, [1,2])
    _test_idsort1_matrix(idsort1, A)
    A = [1,2]
    _test_idsort1_matrix(idsort2, A)
    A = [1,2,3,4]
    _test_idsort1_expected(idsort1, A, [1,4,3,2])
    _test_idsort1_matrix(idsort1, A)
    A = [1,2,3,4]
    _test_idsort1_matrix(idsort2, A)
    A = [1,2,3,4,5,6,7,8,9]
    _test_idsort1_expected(idsort1, A, [1,8,3,6,5,4,7,2,9])
    _test_idsort1_matrix(idsort1, A)
    A = [1,2,3,4,5,6,7,8,9]
    _test_idsort1_matrix(idsort2, A)
    A = [1,3,2,4,6,9,7,8,5]
    _test_idsort1_matrix(idsort1, A)
    A = [1,3,2,4,6,9,7,8,5]
    _test_idsort1_matrix(idsort2, A)
    A = [1,5,2,3] # Already increasing/decreasing sorted
    _test_idsort1_expected(idsort1, A, [1,5,2,3])
    _test_idsort1_matrix(idsort1, A)
    A = [1,5,2,3] # Already increasing/decreasing sorted
    _test_idsort1_matrix(idsort2, A)
    _test_idsort1_expected(idsort2, A, [1,5,2,3])

    #print "Number of tests failed: ", fails

if __name__ == '__main__':
    #test_interleave()
    test_idsort()
