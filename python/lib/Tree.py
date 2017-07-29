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


# Helper functions
def PrintTree(tree, n = 5):
    for row in _getStringRows(tree, n):
        print row

def _getStringRows(t, n):
    if not t:
        return []
    l = _getStringRows(t.left, n)
    r = _getStringRows(t.right, n)
    lindent = 0 if len(l) < 1 else len(l[0])
    rindent = 0 if len(r) < 1 else len(r[0])
    val = t.value
    rows = []
    rows.append(" " * lindent + (str(val) + " " * (n - len(str(val)))) + " " * rindent)
    liter = iter(l)
    riter = iter(r)
    l1 = next(liter, None)
    r1 = next(riter, None)
    while l1 or r1:
        row = " " * lindent if not l1 else l1
        row += " " * n
        row += " " * rindent if not r1 else r1
        rows.append(row)
        l1 = next(liter, None)
        r1 = next(riter, None)
    return rows
