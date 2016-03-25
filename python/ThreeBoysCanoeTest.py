# Three Boys in Canoe from March 15, 2016
# This is the n children version

import sys, os, inspect
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import random
import TwoBoysCanoe
import ThreeBoysCanoe
import ThreeBoysCanoeN

def fillboattest():
    lst = [40,40,50,50,60,60,]
    indices = [0,1,2]
    b, leftover = ThreeBoysCanoeN.fillboat(lst, indices)
    print lst, indices, b.string(), leftover
    indices = [2,4,5]
    b, leftover = ThreeBoysCanoeN.fillboat(lst, indices)
    print lst, indices, b.string(), leftover
    lst = [25,30,35,40,45,60,70,85,95,110,120,135,145]
    indices = [0,1,2,3,4,5]
    b, leftover = ThreeBoysCanoeN.fillboat(lst, indices)
    print lst, indices, b.string(), leftover
    indices = [1,2,4,5]
    b, leftover = ThreeBoysCanoeN.fillboat(lst, indices)
    print lst, indices, b.string(), leftover
   
def client(k, lst):
    print ("Solution for list with %d chilren per boat" % (k)), lst
    for b in ThreeBoysCanoeN.NChildSol(k, lst):
        print b.string()
    if k == 3:
        print "Three child solution: "
        for b in ThreeBoysCanoe.ThreeChildSol(lst):
            print b.string()
        
# Having done the 3-child case, this suggests an approach to the n-child case
# The main difficulty would be to construct the iteratore but python has
# some nice tools for this

fillboattest()
client(2, [30,40,50])
client(3, [30,40,50])
client(3, [30,60,90])
client(4, [30,60,90])
client(3, [10,10,15,70])
client(4, [10,10,15,70])
print "Case k = 3 tests:"
client(3, [40,40,50,50,60,60])
client(3, [30,110,120,130,140])
client(3, [10,10,15,70,70,70,70,130])
client(3, [10,10,10,140,140,140])
client(3, [10,10,140,140,140])
client(3, [40,45,60,70,85,95,110,120,135,145])
client(3, [40,45,60,70,85,95,110,120,135,145,40,45,60,70,85,95,110,120,135,145])
# Test a large sized list
NChildrenList = range(5,26,5)
for NChildren in NChildrenList:
    lst = []
    for i in range(1,NChildren):
        lst.append(random.randint(0,149))
    client(3, lst)
