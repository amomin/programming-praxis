################# Conditional Heap Insert #####################
##################### May 17, 2016  #########################
#
# https://programmingpraxis.com/2016/05/17/conditional-heap-insertion/
#
# This is an Amazon Interview Question:
#
# Given a heap (priority queue), insert an element into the heap
# if the element is not already present in the heap. Your solution
# must work in O(n) time, where n is the number of items in the
# heap.
#
# Your task is to write a program to insert an element into a
# heap if the element is not already present in the heap, in
# logarithmic time.
#
##############################################################

import heapq

# Assumes: h is a list which is heap sorted
# Clearly O(n)
def amazonSol(h, item):
    in_list = False
    i = 0
    while i < len(h):
        if h[i] == item:
            in_list = True
            break
        i += 1
    if not in_list:
        heapq.heappush(h, item)
    return h

# As commenter "Paul" notes, it's even easier than that in python:
def amazonSol2(h, item):
    if item not in h:
        heapq.heappush(h, item)

# Hehe, it's not possible without using a second data structure like a hash table
# to keep track of what's in the heap for searching.
# If you could, then it would be possible to search the heap in log(n) time by
# test inserting the item.  But it's not possible to search a heap in log(n) time.
#
# So there's no solution.
def sol1(h, item):
    return h

def test(method):
    h = [4,12,1,5,9]
    heapq.heapify(h)
    print h, 4 
    print method(h, 4)
    h = [4,12,1,5,9]
    heapq.heapify(h)
    print h, 11
    print method(h, 11)
    h = [4,12,1,5,9]
    heapq.heapify(h)
    print h, 2
    print method(h, 2)

if __name__ == '__main__':
    test(amazonSol)
    test(sol1)
