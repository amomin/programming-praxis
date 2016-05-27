####################### Test Scores ############################
####################### May 24, 2016  ##########################
#
# https://programmingpraxis.com/2016/05/24/test-scores/
#
# Given a list of student names and test scores, compute the average 
# of the top five scores for each student. You may assume each 
# student has as least five scores.
#
######################################################################

import heapq
from random import randint

# Assume xs is a list of dicts with keys "name" and "score"
def sol1(xs):
    topfive = {}
    for x in xs:
        if x["name"] not in topfive:
            topfive[x["name"]] = [0,0,0,0,x["score"]]
        else:
            h = topfive[x["name"]]
            if x["score"] > h[0]:
                heapq.heappop(h)
                heapq.heappush(h,x["score"])
            
    avgs = {}
    for k,v in topfive.iteritems():
        avgs[k] = float(sum(v))/len(v)
    return avgs

if __name__ == '__main__':
    tst = [
        {"name":"A","score":81},
        {"name":"B","score":85},
        {"name":"C","score":81},
        {"name":"A","score":51},
        {"name":"C","score":87},
        {"name":"B","score":71},
        {"name":"A","score":61},
        {"name":"C","score":86},
        {"name":"B","score":83},
        {"name":"C","score":31}
    ]
    print sol1(tst)
    
    tst2 = []
    names = ["A","B","C"]
    for i in range(0,30):
       tst2.append({"name":names[randint(0,2)],"score":randint(30,90)})
    print tst2
    print sol1(tst2)
    
