# Three Boys in Canoe from March 15, 2016
#
# A second approach building a solution by considering all possible ways
# of seating the next child in the boats so far.
# I think this should be O(N^2) time and space

import sys, os, inspect
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import itertools, random, time, math
import Boat, TwoBoysCanoe

def fillboat(lst, indices):
    b = Boat.Boat(len(indices))
    leftover = lst[:]
    offset = 0
    for i in indices:
        if b.fits(lst[i]):
            b.seat(lst[i])
            del leftover[i - offset]
            offset += 1
        else:
            return False, lst
    return b, leftover

def resize_boat_list(k, lst):
    for b in lst:
       b.expand(k)
    return lst

def fullest_boat(k, lst):
    N = len(lst)
    if N == 0:
        return Boat(k), lst
    if k == 0:
        return False, lst
    if N < k:
        b, lo = fullest_boat(k-1, lst)
        if b == False:
            return False, lo
        else:
            b.expand(k)
            return b, lo
    # In this case no combination of children can fill a boat
    if sum(map(lambda(x) : lst[x], range(0,k))) > 150:
        b, lo = fullest_boat(k-1, lst)
        b.expand(k)
        return b, lo
    maxweight = -1
    maxboat = False
    maxboatleftover = lst[:]
    for indices in itertools.combinations(range(0,N), k):
        b, leftover = fillboat(lst, indices)
        if b != False:
            if b.weight() > maxweight:
                maxboat = b
                maxboatleftover = leftover
    return maxboat, maxboatleftover

def greedy(k, lst):
    def _g(k, lst):
        if len(lst) < 1:
            return []
        b, lo = fullest_boat(k, lst)
        if b != False:
            return [b] + _g(k, lo)
        else:
            return False

    lst.sort()
    return _g(k, lst)

if __name__ == '__main__':
    def printgreedy(k, lst):
        print map(lambda(x): x.string(), greedy(k, lst))
   
    def tstfullest(k, lst):
        b, lo =  fullest_boat(k, lst)
        print b.string(), lo

    for i in range(15,25):
        lst = []
        for j in range(0,i):
            lst.append(random.randint(20,60))
        print lst
        lst.sort()
        printgreedy(3, lst)
        printgreedy(4, lst)
        printgreedy(5, lst)
