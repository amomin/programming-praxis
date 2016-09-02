#!/usr/bin/python
#################################### Min-Min-Max ###################################
################################# August 12, 2016  #################################
#
# https://programmingpraxis.com/2016/08/12/min-min-max/
#
# Given an unsorted array of integers, find the smallest number in the
# array, the largest number in the array, and the smallest number between
# the two array bounds that is not in the array. For instance, given the
# array [-1, 4, 5, -23, 24], the smallest number is -23, the largest number
# is 24, and the smallest number between the array bounds is -22. You may
# assume the input is well-formed.
#
#####################################################################################

# O(1) space, O(n**2) time, but short
def min_min_max_0(l):
    if len(l) == 0: return False, False, False
    m = min(l)
    M = max(l)
    x = m
    while x in l: x += 1
    if x > M: x = False
    return m,x,M


# O(M) space, O(n) time 
# where n = number of elements in l
# M = difference between the max and the min in l
def min_min_max(l):
    if len(l) == 0: return False, False, False
    _min=l[0]
    _max=l[0]
    for x in l:
        if x < _min: _min = x
        if x > _max: _max = x
    table=[False]*(_max-_min+1)
    for x in l:
        table[x-_min] = True
    min_out = False
    for i in range(len(table)):
        if not table[i]:
            min_out = _min + i
            break
    return _min,min_out,_max

# O(1) space, O(nlog(n)) time but sorts the input array
def min_min_max_2(l):
    if len(l) == 0: return False, False, False
    m = min(l)
    M = max(l)
    l.sort()
    x = m
    for i in range(1,len(l)):
        x += 1
        if l[i] != x:
            break
    if x >= M: x = False
    return m,x,M

if __name__ == '__main__':
    print min_min_max([-1,4,5,-23,24])
    print min_min_max([-100,-99,0,50])
    print min_min_max([0,-99,50,-100])
    print min_min_max([])
    print min_min_max([1])
    print min_min_max([3,1,2])
    
    print min_min_max_0([-1,4,5,-23,24])
    print min_min_max_0([-100,-99,0,50])
    print min_min_max_0([0,-99,50,-100])
    print min_min_max_0([])
    print min_min_max_0([1])
    print min_min_max_0([3,1,2])
    
    print min_min_max_2([-1,4,5,-23,24])
    print min_min_max_2([-100,-99,0,50])
    print min_min_max_2([0,-99,50,-100])
    print min_min_max_2([])
    print min_min_max_2([1])
    print min_min_max_2([3,1,2])
