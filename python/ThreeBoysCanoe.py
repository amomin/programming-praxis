# Three Boys in Canoe from March 15, 2016
#
# Approach is very slow.  Already for 25 random children it takes a 
# long time (> 1 minute) to solve.  There are some optimizations one could try
# but I think a better approach might be necessary.  Perhaps there is a better
# algorithm.
# I would probably substitute a non-optimal but faster greedy solution
# which should perform decently in most cases.

import sys, os, inspect
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import TwoBoysCanoe

# Define a data structure to represent canoes
class Boat:
    def __init__(self):
        self.s1 = 0
        self.s2 = 0
        self.s3 = 0

    def fits(self, x):
        return (self.s3 == 0) and (self.weight() + x <= 150)

    def weight(self):
        return self.s1 + self.s2 + self.s3

    def string(self):
        return ("(%d,%d,%d)" % (self.s1,self.s2,self.s3))

    def seat(self, x):
        if not self.fits(x):
            raise Exception("Does not fit on boat")
        else:
            if self.s1 == 0:
                self.s1 = x
            elif self.s2 == 0:
                self.s2 = x
            else:
                self.s3 = x

    def non_empty_seats(self):
        i = 0
        if self.s1 != 0:
            i += 1
        if self.s2 != 0:
            i += 1
        if self.s3 != 0:
            i += 1
        return i

# Solution from Two Children problem
def TwoChildrenSol(lst):
    lst.sort()
    sol = []
    sol2 = TwoBoysCanoe.canoes(lst)
    for (x,y) in sol2:
        b = Boat()
        b.seat(x)
        if y:
            b.seat(y)
        sol.append(b)
    return sol

# Base cases of the recursion
def basecase(N, lst):
    if N == 0:
        return []
    if lst[N-1] > 150:
        return False
    if N == 1:
        b = Boat()
        b.seat(lst[0])
        return [b]
    if N == 2:
        b = Boat()
        b.seat(lst[0])
        if b.fits(lst[1]):
            b.seat(lst[1])
            return [b]
        else:
            b2 = Boat()
            b2.seat(lst[1])
            return [b,b2] 

# The inducting step
# Fit as many as you can in the boat
# and then find the optimal fit of the
# leftovers
# Combine the two solutions and compare to the optimal
# solution
def fillboat(lst, i, j, k):
    b = Boat()
    b.seat(lst[i])
    leftover = lst[:]
    del leftover[i]
    if b.fits(lst[j]):
        b.seat(lst[j])
        del leftover[j-1]
        if b.fits(lst[k]):
            b.seat(lst[k])
            del leftover[k-2]
    return b, leftover

# Enumerative solution
# Not fast but returns an optimal (fewest boats)
# Consider all triplets with sum <= 150
# Put them on a boat.  Solve the problem for the remaining
# children.  Take the least solution.
#
# We speed this up by computing the solution for the two children problem,
# and then considering all triplets of children which can fill a boat,
# adding them to the solution obtained by removing them from the list.
# We keep track of such optimal solutions and return the first one found.
def ThreeChildSol(lst):
    N = len(lst)
    lst.sort()
    if N < 3:
        return basecase(N, lst)
    if lst[N-1] > 150:
        # No solution so just stop
        return False
    # In this case the two children solution solves the problem
    # since no three children can fit in a boat
    if lst[0] + lst[1] + lst[2] > 150:
        return TwoChildrenSol(lst)
    # Use the two children solution as a benchmark
    # This allows us to consider only triplets of children which fit in a boat
    # henceforth, which means we check much fewer cases recursively
    best = TwoChildrenSol(lst)
    nbestsofar = len(best)
    for i in range(0,N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                b, leftover = fillboat(lst, i, j, k)
                # Only continue if canoe is full
                # Since we already checked the two children solutions
                #### The simplest case solution would skip this conditional check
                #### and just compute recursively in all cases, but this gets
                #### to be rather expensive even for fairly short inputs
                if b.non_empty_seats() == 0:
                    ans = ThreeChildSol(leftover)
                    if len(ans) + 1 < nbestsofar:
                        nbestsofar = len(ans) + 1
                        best = [b] + ans
    return best
