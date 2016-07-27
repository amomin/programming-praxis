#!/usr/bin/python
############################# Array Manipulation  #############################
###############################  July 22, 2016  ###############################
#
# https://programmingpraxis.com/2016/07/22/array-manipulation/
#
# Given an array of positive integers, replace every element with the least
# greater element to its right. If there is no greater element to its right,
# replace it with -1. For instance, given the array [8, 58, 71, 18, 31,
# 32, 63, 92, 43, 3, 91, 93, 25, 80, 28], the desired output is [18,
# 63, 80, 25, 32, 43, 80, 93, 80, 25, 93, -1, 28, -1, -1].
#
# Your task is to write the program that manipulates an array as described above.
#
#################################################################################

def naive(arr):
    initMax = max(arr) + 1
    for i in range(0,len(arr)):
        # How to init?
        minMaxSoFar = initMax
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[i] and arr[j] < minMaxSoFar:
                minMaxSoFar = arr[j]
        if minMaxSoFar < initMax:
            arr[i] = minMaxSoFar
        else:
            arr[i] = -1

# Same but more concise
def naive2(arr):
    initMax = max(arr) + 1
    for i in range(0,len(arr)):
        rightValuesGreater = filter(lambda x : x > arr[i], arr[i:])
        if len(rightValuesGreater) > 0:
            arr[i] = min(rightValuesGreater)
        else:
            arr[i] = -1

# Model a binary tree
class Tree:
    # Store left, right, parent pointers, and the value
    left = False
    right = False
    parent = False
    value = False
    
    def __init__(self, val):
        self.value = val
        self.left = False
        self.right = False
        self.parent = False

    def insert(self, val):
        if val < self.value:
            if self.left != False:
                return self.left.insert(val)
            else:
                self.left = Tree(val)
                self.left.parent = self
                return self.left
        elif val > self.value:
            if self.right != False:
                return self.right.insert(val)
            else:
                self.right = Tree(val)
                self.right.parent = self
                return self.right
        else:
            return self
    
    # Return the least value in the tree greater than v
    # Return -1 if no such value
    def minGreater(self, v):
        if self.value <= v:
            if self.right == False:
                return -1
            return self.right.minGreater(v)
        if self.value > v:
            if self.left != False:
                temp = self.left.minGreater(v)
                if temp != -1:
                    return temp
            return self.value

# Use a binary tree instead
# Though the worst case is still O(n^2) in case the tree is linear,
# more often the tree's height will be comparable to log(n), and the
# insert/minGreater operations will take log(n), so the expected runtime
# should be O(nlog(n))
def binaryTree(arr):
    N = len(arr)
    root = Tree(arr[N -1])
    arr[N - 1] = -1
    for i in range(N - 2, -1, -1):
        temp = root.minGreater(arr[i])
        node = root.insert(arr[i])
        arr[i] = temp

import random,time

def testBinaryOnRandomList(N, minM, maxM):
    arr = range(0,N)
    print "Building list"
    arr = map(lambda x: minM + random.randint(0,maxM - minM), arr)
    print "Done building list"
    arrBin = list(arr)
    t2 = time.time()
    binaryTree(arrBin)
    t2 = time.time() - t2
    print "Binary tree time:", t2

def testCompareNaiveBinaryOnRandomList(N, minM, maxM):
    arr = range(0,N)
    arr = map(lambda x: minM + random.randint(0,maxM - minM), arr)
    arrNaive = list(arr)
    arrBin = list(arr)
    t1 = time.time()
    naive2(arrNaive)
    t1 = time.time() - t1
    t2 = time.time()
    binaryTree(arrBin)
    t2 = time.time() - t2
    print "Naive time:       ", t1
    print "Binary tree time: ", t2
    errors = []
    for i in range(len(arr)):
        if arrNaive[i] != arrBin[i]:
            errors.append("Solutions differ in position i:", i, arr[i], arrBin[i])
    if len(errors) == 0:
        print "No difference between solutions"
    else:
        for e in errors:
            print e

def testExample():
    arr  = [8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28]
    arr2 = [8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28]
    arr3 = [8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28]
    naive     (arr )
    naive2    (arr2)
    binaryTree(arr3)
    print "Original:", arr
    print "Naive:   ", arr2
    print "Binary:  ", arr3

if __name__ == '__main__':
    print "Testing example"
    testExample()
    N = 1000
    print "Comparing binary and naive solutions on a random list of size", N
    testCompareNaiveBinaryOnRandomList(N, 10, 100000)
    N = 2000
    print "Comparing binary and naive solutions on a random list of size", N
    testCompareNaiveBinaryOnRandomList(N, 10, 100000)
    N = 4000
    print "Comparing binary and naive solutions on a random list of size", N
    testCompareNaiveBinaryOnRandomList(N, 10, 100000)
    N = 50000
    print "Testing binary solution on a random list of size",N
    testBinaryOnRandomList(N, 10, 100000)
