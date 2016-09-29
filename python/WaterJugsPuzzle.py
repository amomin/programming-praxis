############### A Common Interview Question ###################
################### September 13, 2016  #######################
#
# https://programmingpraxis.com/2016/09/23/water-jugs-puzzle/
#
# There are various puzzles in which water is poured from one jug to another 
# to reach a desired amount of water. In the version we consider today, 
# we have two jugs, an unlimited amount of water to fill them, and a drain 
# into which we can pour an unlimited amount of water. The two jugs have 
# known capacities, but it is not possible to accurately measure portions 
# of a jug.
# 
# As an example, we wish to obtain four gallons of water, using jugs of capacities 
# three and five gallons. Starting with two empty jugs, it is possible 
# to obtain four gallons of water using the following six steps:
#
# * Fill the five-gallon jug.
# * Pour three gallons from the five-gallon jug to the three-gallon jug, 
# leaving two gallons in the five-gallon jug.
# * Empty the three-gallon jug.
# * Pour two gallons from the five-gallon jug to the three-gallon jug, leaving 
# the five-gallon jug empty and two gallons in the three-gallon jug.
# * Fill the five-gallon jug.
# * Pour one gallon from the five-gallon jug into the three-gallon jug, filling 
# it, leaving the desired four gallons in the five-gallon jug.
#
# Bruce Willis figured that out once; so too do thousands of school children 
# every year.
# 
# Your task is to write a program that solves this kind of water-jug problem 
# using the minimum number of steps (filling a jug, emptying a jug, or 
# pouring one jug into the other). 
#
###############################################################

import Queue

# bfs? dfs?
# dp?
# recursion?
# I think we'll try a BFS
# Should do a gcd check first to make sure a solution
# is possible.
def jug(x, y, v):
    q = Queue.Queue()
    q.put((0,0))
    prev = {}
    prev[(0,0)] = ""
    while not q.empty():
        j = q.get_nowait()
        p = ""
        if j in prev:
            p = prev[j]
        if j[0] == v:
            a = []
            while j in prev:
                a.insert(0,j)
                j = prev[j]
            a.pop(0)
            return a
        if j[1] == v:
            a = []
            while j in prev:
                a.insert(0,j)
                j = prev[j]
            a.pop(0)
            return a
        # Fill 1
        n = (x,j[1])
        if not n in prev:
            prev[(x,j[1])] = j
            q.put((x,j[1]))
        # Fill 2
        n =(j[0],y)
        if not n in prev:
            prev[(j[0],y)] = j
            q.put((j[0],y))
        # Empty 1
        n = (0,j[1])
        if not n in prev:
            prev[n] = j
            q.put(n)
        # Empty 2
        n = (j[0],0)
        if not n in prev:
            prev[n] = j
            q.put(n)
        # Pour 2 -> 1
        z = min(x,j[0]+j[1])
        n = (z,j[1]-(z-j[0]))
        if not n in prev:
            prev[n] = j
            q.put(n)
        # Pour 1 -> 2
        z = min(y,j[0]+j[1])
        n =(j[0]-(z-j[1]),z)
        if not n in prev:
            prev[n] = j
            q.put(n)
    return []

def test(x,y,v,expected):
    a1 = jug(x,y,v)
    if len(a1) != len(expected):
        print "Solution lenght does not match expected length"
        print a1
        print expected
    else:
        for i in range(len(a1)):
            if a1[i] != expected[i]:
                print "Solutions differ in place ", i
    print "Done test"
    return

if __name__ == '__main__':
    test(3,5,4,[(0,5),(3,2),(0,2),(2,0),(2,5),(3,4)])
    

