#!/usr/bin/python
################ Highly Composite Numbers With Priority Queues  ###############
############################## July 15, 2016  #################################
#
# https://programmingpraxis.com/2016/07/15/highly-composite-numbers-using-priority-queues/
#
#A different solution to the previous exercise exploits the form of highly
# composite numbers, which always consists of small primes to large exponent,
# so we can specify the highly composite number using only the exponent;
# for instance, 64221111 represents the number 26 * 34 * 52 * 72 * 111 *
# 131 * 171 * 191 = 293318625600. Since the exponents must be non-increasing,
# there are five possibilities for a larger highly composite numbers,
# represented using the power-notation as 74221111, 65221111, 64321111,
# 64222111, and 642211111. Thus, we find composite numbers by starting
# with the null power-list, which equates to the number 20 = 1, then add
# all possible successors to a priority queue, pop the successors in order,
# check each for a new record number of divisors, and push the successors
# of that number back on to the priority queue.
#
# Your task is to generate the sequence of highly composite numbers using 
# a priority queue.
#################################################################################

import heapq

N = 1000
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]

def nxt(item):
    (n, lst) = item
    newLists = []
    for i in range(0,len(lst)):
        newList = list(lst)
        newList[i] = lst[i] + 1
        newn = n*primes[i]
        newItem = (newn, newList)
        newLists.append(newItem)
    newList = list(lst)
    newList.append(1)
    newn = n * primes[len(lst)]
    newLists.append((newn, newList))
    return newLists

def nFactors(itemList):
    return reduce(lambda x, y: x * y, map(lambda x : x + 1, itemList), 1) 

def hcnUpTo(N):
    hcn = []
    maxFactorsSoFar = -1

    h = [(1,[])]
    n = 1

    while n < N:
        (n, flist) = heapq.heappop(h)
        if n > N:
            break
        nf = nFactors(flist)
        if nf > maxFactorsSoFar:
            hcn.append((n,flist))
            maxFactorsSoFar = nf
            newLists = nxt((n,flist))
            for l in newLists:
                heapq.heappush(h,l)
    return hcn
    
if __name__ == '__main__':
    
    N = int(input("Enter a number"))
    hcn = hcnUpTo(N)
    for item in hcn:
        print item[0]
