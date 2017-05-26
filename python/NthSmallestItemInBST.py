################### Nth Smallest Item in Binary Search tree #######################
############################## May 25, 2017  ######################################
#
# A binary search tree is a binary tree in which all nodes in the left subtree
# are less than the current node and all nodes in the right subtree are greater
# than the current node. Items arrive in random order, are inserted into the
# binary search tree, and an in-order traversal produces the items in ascending
# order.
#
# Your task is to write a program that finds the nth smallest item in a binary
# search tree, without enumerating all of the items in the tree. When you are
# finished, you are welcome to read or run a suggested solution, or to post
# your own solution or discuss the exercise in the comments below.
#
###################################################################################

class Node:
    value = 0
    left = None
    right = None
    size = 0

    def __init__(self, v):
        self.value = v

def kth_smallest(node, k):
    if node == None:
        return None
    v = kth_smallest(node.left, k)
    if v == None:
        s = node.left.size if node.left else 0
        if s + 1 == k:
            return node.value
        w = kth_smallest(node.right, k - s - 1)
        if w == None:
            node.size = 1 + (node.left.size if node.left else 0) \
                + (node.right.size if node.right else 0)
            return None
        return w
    return v

if __name__ == '__main__':
    # Full tree, depth 2
    t = Node(100)
    t.left = Node(50)
    t.right = Node(150)
    for i in range(0,5):
        print kth_smallest(t, i)
    # Full tree, depth 3
    t = Node(100)
    t.left = Node(50)
    t.left.left = Node(25)
    t.left.right = Node(75)
    t.right = Node(150)
    t.right.left = Node(125)
    t.right.right = Node(175)
    for i in range(0,9):
        print kth_smallest(t, i)
    # Partial tree
    t = Node(100)
    t.left = Node(50)
    t.left.right = Node(75)
    t.right = Node(150)
    t.right.left = Node(125)
    for i in range(0,9):
        print kth_smallest(t, i)
