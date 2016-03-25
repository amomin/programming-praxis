# Three Boys in Canoe from March 15, 2016
#
# This is the n children version.  This is probably very slow for reasonable sized
# lists.

import sys, os, inspect
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import itertools
import TwoBoysCanoe

# Define a data structure to represent canoes
class Boat:
    def __init__(self, k):
        self.seats = [0] * k
        self.k = k

    def fits(self, x):
        return (self.seats[self.k-1] == 0) and (self.weight() + x <= 150)

    def weight(self):
        return sum(self.seats)

    def string(self):
        res = '('
        for x in self.seats:
            res += str(x) + ', '
        return res[:len(res) - 2] + ')'

    def seat(self, x):
        if not self.fits(x):
            raise Exception("Does not fit on boat")
        if not (self.seats[self.k-1] == 0):
            raise Exception("Boat is full")
        i = 0
        while self.seats[i] != 0:
            i += 1
        self.seats[i] = x
            
    def non_empty_seats(self):
        i = 0
        while (i < self.k) and (self.seats[i] != 0):
            i += 1
        return i

    def expand(self, newk):
        if newk < self.k:
            raise Exception("New boat has fewer seats", newk, self.seats)
        newseats = [0] * newk
        for i in range(0,self.k):
            newseats[i] = self.seats[i]
        self.seats = newseats
        self.k = newk

# Solution from Two Children problem
def TwoChildrenSol(lst):
    lst.sort()
    N = len(lst)
    if N == 0:
        return []
    if N == 1:
        b = Boat(1)
        b.seat(lst[0])
        return [b]
    sol = []
    sol2 = TwoBoysCanoe.canoes(lst)
    for (x,y) in sol2:
        b = Boat(2)
        b.seat(x)
        if y:
            b.seat(y)
        sol.append(b)
    return sol

# The inducting step
# Fit as many as you can in the boat
# and then find the optimal fit of the
# leftovers
# Combine the two solutions and compare to the optimal
# solution
def fillboat(lst, indices):
    b = Boat(len(indices))
    leftover = lst[:]
    offset = 0
    for i in indices:
        if b.fits(lst[i]):
            b.seat(lst[i])
            del leftover[i - offset]
            offset += 1
    return b, leftover


def resize_boat_list(k, lst):
    for b in lst:
       b.expand(k)
    return lst
    

# Enumerative solution
# Not fast but returns an optimal solution
# Consider all tuples with sum <= 150
# Put them on a boat.  Solve the problem for the remaining
# children.  Take the least solution.
def NChildSol(k, lst):
    N = len(lst)
    lst.sort()
    if k < 3:
        return resize_boat_list(k, TwoChildrenSol(lst))
    if N < k:
        return resize_boat_list(k, NChildSol(N, lst))
    if lst[N-1] > 150:
        # No solution so just stop
        return False
    # In this case no combination of children can fill a boat so
    # descent to k-1 case
    # since no three children can fit in a boat
    if sum(map(lambda(x) : lst[x], range(0,k))) > 150:
        return resize_boat_list(k, NChildSol(k-1, lst))
    # Use the k-1 children solution as a benchmark
    # This allows us to consider only tuples of children which fit in a boat
    # henceforth, which means we check much fewer cases recursively
    best = NChildSol(k-1, lst)
    nbestsofar = len(best)
    for indices in itertools.combinations(range(0,N), k):
        b, leftover = fillboat(lst, indices)
        if b.non_empty_seats() == k:
            ans = NChildSol(k, leftover)
            if len(ans) + 1 < nbestsofar:
                nbestsofar = len(ans) + 1
                best = [b] + ans
    return resize_boat_list(k, best)
