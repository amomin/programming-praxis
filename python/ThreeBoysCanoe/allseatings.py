# Three Boys in Canoe from March 15, 2016
#
# A second approach building a solution by considering all possible ways
# of seating the next child in the boats so far.
# I think this should be O(N^2) time and space

import sys, os, inspect
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import math
import Boat, TwoBoysCanoe

def allseatings(sofar, lst):
    if len(lst) == 0:
        return sofar
    lst.sort()
    lst.reverse()
    if (lst[0] > 150):
        return False
    if len(sofar) == 0:
        b = Boat.Boat3()
        b.seat(lst[0])
        return allseatings([[b]], lst[1:])
    head = lst[0]
    tail = lst[1:]
    newsols = []
    for sol in sofar:
        for i in range(0,len(sol)):
            b = sol[i]
            if b.fits(head):
                ns = []
                nb = b.clone()
                nb.seat(head)
                for j in range(0,len(sol)):
                    if j != i:
                        ns.append(sol[j])
                    else:
                        ns.append(nb)
                newsols.append(ns)
        ns = sol[:]
        nb = Boat.Boat3()
        nb.seat(head)
        ns.append(nb)
        newsols.append(ns)
    return allseatings(newsols, tail)

def client( lst):
    print "Three child solution: "
    idx = 1
    for sol in allseatings([], lst):
        print "Solution ", idx
        idx += 1
        for b in sol:
            print b.string()

if __name__ == '__main__':
    # The number of seatings grows exponentially or maybe even superexponentially
    for i in range(5,12):
        lst = range(5,5+i)
        sols = allseatings([], lst)
        print "Log Number of solutions ", i, " is ", math.log(len(sols))
