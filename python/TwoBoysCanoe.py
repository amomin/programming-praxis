# Two Boys in Canoe from March 11, 2016
#
# Like the haskell solution but uses a doubly-linked list
# 

class Node:
    n = False
    p = False
    val = 0

    def __init__(self,n):
        self.val = n

# Converts arr to a doubly linked list
# Returns pointers to the head and tail of the list
def arrToDLinked(arr):
    c = Node(arr[0])
    lo = c
    for i in range(1,len(arr)):
        n = Node(arr[i])
        c.n = n
        n.p = c
        c = n
    hi = n
    return (lo,hi)
  
# If you use a bucket or radix sort this will be O(n)
def canoes(arr):
    arr.sort()
    (lo,hi) = arrToDLinked(arr)
    return _canoes(lo,hi)

# Pass the pointers
def _canoes(lo, hi):
    ans = []
    if (hi.val > 150):
        return False
    while (lo.n != hi and lo != hi):
        if (lo.val + hi.val <= 150):
            ans.append((lo.val,hi.val))
            lo = lo.n
            hi = hi.p
        else:
            ans.append((False,hi.val))
            hi = hi.p
    if (lo == hi):
        ans.append((False, lo.val))
    else:
        if (lo.val + hi.val <= 150):
            ans.append((lo.val,hi.val))
        else:
            ans.append((False,hi.val))
            ans.append((False,lo.val))
    return ans
        
if __name__ == '__main__':
    arr = [140,60,130,80,50,70,90]
    print canoes(arr)
    arr = [140,60,130,80,50,70,70,70,10]
    arr.sort()
    (lo,hi) = arrToDLinked(arr)
    print arr
    print canoes(arr)
