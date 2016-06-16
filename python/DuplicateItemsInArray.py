#!/usr/bin/python
########################### Duplicate Items in Array ###########################
################################ June 14, 2016  ################################
#
# https://programmingpraxis.com/2016/06/14/duplicate-items-in-an-array/
#
# First, write a program that, given an array of integers in unsorted 
# order, finds the single duplicate number in the array. For instance, 
# given the input [1,2,3,1,4], the correct output is 4.
# 
# Second, write a program that, given an array of integers in unsorted order,
# finds all of the multiple duplicate numbers in the array. For instance,
# given the input [1,2,3,1,2,4,1], the correct output is [1,2,1].
#
#################################################################################

# Using hash table - Space O(n) extra, time O(n)
def duplicateWithHashTable(ns):
    n = len(ns)
    _dict = {}
    i = 0
    while i < n:
        if ns[i] in _dict:
            return ns[i]
        _dict[ns[i]] = 0
        i += 1
    return False

# As praxis points out, if you can't afford the extra space then
# you can sort and find the first duplicate
# Space O(1) extra, time O(n log(n))
# Assumes log-linear in-place sort (e.g. heap sort, quick sort is fine
# in most cases)
def duplicateBySort(ns):
    ns.sort()
    i = 0
    m = len(ns) - 1
    while i < m:
        if ns[i + 1] == ns[i]:
            return ns[i]
        i += 1
    return False

# Same as solution with hash table but collect all duplicates in order encountered
def duplicates(ns):
    _dict = {}
    dupes = []
    i = 0
    while i < len(ns):
        if ns[i] in _dict:
            dupes.append(ns[i])
        _dict[ns[i]] = 0
        i += 1
    return dupes

if __name__ == '__main__':
    # Not thoroughly tested
    print duplicateWithHashTable([1,2,3,1,4])
    print duplicateBySort([1,2,3,1,4])
    print duplicateWithHashTable([1,2,3,2,4])
    print duplicateBySort([1,2,3,2,4])
    print duplicates([1,2,3,1,4])
    print duplicates([1,2,3,1,2,4,1])
