# Three Boys in Canoe from March 15, 2016
# This is the n children version

import sys, os, inspect
print os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import random, math, time
import Boat, TwoBoysCanoe, Original, NChildren, greedy

def fillboattest():
    lst = [40,40,50,50,60,60,]
    indices = [0,1,2]
    b, leftover = NChildren.fillboat(lst, indices)
    print lst, indices, b.string(), leftover
    indices = [2,4,5]
    b, leftover = NChildren.fillboat(lst, indices)
    print lst, indices, b.string(), leftover
    lst = [25,30,35,40,45,60,70,85,95,110,120,135,145]
    indices = [0,1,2,3,4,5]
    b, leftover = NChildren.fillboat(lst, indices)
    print lst, indices, b.string(), leftover
    indices = [1,2,4,5]
    b, leftover = NChildren.fillboat(lst, indices)
    print lst, indices, b.string(), leftover
   
def client(k, lst):
    print ("Solution for list with %d chilren per boat" % (k)), lst
    for b in NChildren.NChildSol(k, lst):
        print b.string()

def compareNwith3(lst):
    k = 3
    print ("Solution for list with %d chilren per boat" % (k)), lst
    for b in NChildren.NChildSol(k, lst):
        print b.string()
    if k == 3:
        print "Three child solution: "
        for b in Original.ThreeChildSol(lst):
            print b.string()

#fillboattest()
#client(2, [30,40,50])
#client(3, [30,40,50])
#client(3, [30,60,90])
#client(4, [30,60,90])
#client(3, [10,10,15,70])
#client(4, [10,10,15,70])
#print "Case k = 3 tests:"
#compareNwith3([40,40,50,50,60,60])
#compareNwith3([30,110,120,130,140])
#compareNwith3([10,10,15,70,70,70,70,130])
#compareNwith3([10,10,10,140,140,140])
#compareNwith3([10,10,140,140,140])
#compareNwith3([40,45,60,70,85,95,110,120,135,145])
#compareNwith3([40,45,60,70,85,95,110,120,135,145,40,45,60,70,85,95,110,120,135,145])

#greedy
def time_greedy():
    NChildrenList = range(5,100,2)
    for num_children in NChildrenList:
        t = time.time()
        lst = []
        for i in range(1,num_children):
            lst.append(random.randint(20,100))
        sol = greedy.greedy(3, lst)
        sollength = len(sol)
        elapsed = time.time() - t
        print "For ", num_children, " took time ", elapsed, " solution has length", sollength

time_greedy()

# Check that time growth is superexponential
def time_original():
    NChildrenList = range(5,20,2)
    for num_children in NChildrenList:
        t = time.time()
        lst = []
        for i in range(1,num_children):
            lst.append(random.randint(20,100))
        sol = NChildren.NChildSol(3, lst)
        elapsed = time.time() - t
        print "For ", num_children, " took log time ", math.log(elapsed)
