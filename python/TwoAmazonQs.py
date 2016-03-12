# February 26 2016
#
# 1. Create a set data structure that provides the following operations, which 
# must all operate in constant time: insert, delete, member?, and random
# The random operation should return a random element from the set.
#
# and
#
# 2. Given an array, find the first element that appears an even number of times.

import random

class RSet:
    
    dict = {}

    def isMember(self, x):
        return x in self.dict

    def insert(self, x):
        self.dict[x] = True
    
    def delete(self, x):
        del self.dict[x]

    # Is this really O(1)?
    # AFAIK building the key list would be O(n)
    # making this O(n)
    # Really need to get into the details of the hash table to make this work
    # Generally the number of buckets is roughly the same size as the numebr
    # of items in the hash table, so you should be able to
    # pick a random bucket and a random element of that bucket in constant
    # time on average.  The distribution is not quite uniform though
    # because items in larger buckets will be selected less often.
    def random(self):
        return random.choice(self.dict.keys())

def sol2(arr):
    dict = {}
    for i in range(0, len(arr)):
        v = arr[i]
        if v in dict:
            dict[v] += 1
        else:
            dict[v] = 1
    i = 0
    while i < len(arr):
        if dict[arr[i]] % 2 ==0:
            return arr[i]
        i += 1
    return False

if __name__ == '__main__':
    print "Example of sol2"
    arr = [1,2,3,4,1,5,2,6,3,1,7,2,1,1,8,4,9,3,3,10,11]
    print arr
    print sol2(arr)
    print "Should be 3"
