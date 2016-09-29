############### A Common Interview Question ###################
################### September 13, 2016  #######################
#
# https://programmingpraxis.com/2016/09/27/maximum-product-of-three/
#
# Today's exercise comes from the end-of-chapter exercises in the sorting 
# chapter of a programming textbook:
# 
# Write a program that finds the maximum product of three numbers in a 
# given array of integers.
# 
# Your task is to write the desired program.
#
###############################################################

# Possibilities:
#
# If all numbers are negative, take the largest three
# If all numbers positive, take the largest three
# If at least two negative numbers, consider also the two smallest times the largest
# 
# Zero negative (All positive)
# One  negative, two positive
# One  negative, many positive
# Two  negative, one positive
# Two  negative, multiple positive
# Three negative, zero positive (all negative)
# Three negative, one or two positive
# Many negative and positive
#
def max_product_of_three(l):
    if len(l) < 3:
        print "List too small"
        return 0
    negs = filter(lambda(x): x < 0, l)
    pos  = filter(lambda(x): x >= 0, l)
    negs = sorted(negs)
    pos  = sorted(pos, reverse=True)
    if len(negs) == 0:
        return pos[0] * pos[1] * pos[2]

    if len(negs) == 1:
        if len(pos) == 2:
            return negs[0] * pos[0] * pos[1]
        else:
            return pos[0] * pos[1] * pos[2]

    # len(negs)>=2
    if (len(pos)==0):
        x = len(negs)
        return negs[x-1]*negs[x-2]*negs[x-3]
    if (len(pos)==1):
        x = len(negs)
        return negs[0]*negs[1]*pos[0]
    if (len(pos)==2):
        # Still need 2 negs * 1 pos
        x = len(negs)
        return negs[0]*negs[1]*pos[0]
    # Both pos/negs have at least 2 elements
    p1 = negs[0] * negs[1]
    p2 = pos[1]*pos[2]
    return pos[0]*max(p1,p2)

import random

def rand_test(tests,n,l,r):
    for t in range(tests):
        a = [l + int(random.random()*(r-l+1))  for i in range(n)]
        expected = max([a[i]*a[j]*a[k] for i in range(n) \
                                       for j in range(i+1,n) \
                                       for k in range(j+1,n)])
        print a
        print expected, "?=", max_product_of_three(a)

if __name__ == '__main__':
    # All positive
    # [4,2,5,6]         -> 4*5*6
    # [1,2,3,4]         -> 2*3*4
    print "Expect: ", 120
    print max_product_of_three([4,2,5,6])
    print "Expect: ", 24
    print max_product_of_three([1,2,3,4])
    # All negative
    # [-4,-3,-2,-1]     -> -1*-2*-3
    print "Expect: ", -6
    print max_product_of_three([-4,-3,-2,-1])
    # One negative, two positive
    # [-7,1,2]          -> -7*1*2
    print "Expect: ", -14
    print max_product_of_three([-7,1,2])
    # One negative, many positive
    # [-7,4,5,6]        -> 4*5*6
    print "Expect: ", 4*5*6
    print max_product_of_three([-7,4,5,6])
    # Two negative, one positive
    # [-4,-5,3]       -> -4*-5*3
    print "Expect: ", 60
    print max_product_of_three([-4,-5,3])
    # Three negative, one positive
    # [-3,-1,-1,3]   -> 9
    print "Expect: ", 9
    print max_product_of_three([-3,-1,-1,3])
    # Two negative, two positive
    # [-4,-5,2,3]       -> -4*-5*3
    print "Expect: ", 60
    print max_product_of_three([-4,-5,2,3])
    # Two negative, three positive
    print "Expect: ", 30
    print max_product_of_three([-2,-3,1,4,5])
    print "Expect: ", 60
    print max_product_of_three([-2,-3,3,4,5])
    # Many negative and positive
    # [-6,-2,-3,1,4,5]  -> -6*-3*5
    print "Expect: ", 90
    print max_product_of_three([-6,-2,-3,1,4,5])
    # [-1,-2,-3,1,4,5]  -> -2*-3*5
    print "Expect: ", 30
    print max_product_of_three([-1,-2,-3,1,4,5])
    # Do some random tests to see if any cases were missed
    rand_test(5,4,-5,5)
    rand_test(5,4,-5,20)
    rand_test(5,5,-10,10)
    rand_test(5,6,-10,10)
