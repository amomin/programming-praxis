#!/usr/bin/python
########################## ReRooting a Binary Search Tree ##########################
################################### July 27, 2017  #################################
#
# https://programmingpraxis.com/2017/07/28/rerooting-a-binary-search-tree/
#
# Write a program that takes a binary search tree and a given node of the tree and
# returns a new binary search tree with the given node at its root, changing as few
# nodes within the tree as necessary.
#
####################################################################################

from lib.Tree import Tree, PrintTree

def Reroot(tree, node):
    if tree == node:
        return
    if node.value < tree.value:
        Reroot(tree.left, node)
        s = node.right
        node.right = tree
        tree.left = s
        return node
    elif node.value > tree.value:
        Reroot(tree.right, node)
        s = node.left
        node.left = tree
        tree.right = s
        return node

def _MakeTree(l):
    t = Tree(l[0])
    for v in l[1:]:
        t.insert(v)
    return t

def main():
    t = _MakeTree([40, 20, 30, 10, 50, 45, 47, 48, 15, 5])
    PrintTree(t)
    node = t.right.left
    t = Reroot(t, node)
    PrintTree(t)

if __name__ == '__main__':
    main()
