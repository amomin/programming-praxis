### SUM And Xor
### April 1 2016
###
# 
# I don't know the origin of it, but today's exercise must be either a 
# homework problem or an interview question:
#
# Assume there are two positive integers a and b that have sum s and XOR 
# x. Given an s on the range [2, 1012] and x on the range [0, 1012], find 
# a list of possible values of the ordered pairs (a, b). For instance, 
# given s = 9 and x = 5, there are four possible pairs: (2, 7), (7, 2), 
# (3, 6) and (6, 3).
#
# Your task is to write a program that finds the pairs.

# Don't know if there's a built-in python xor oepration
# so build it from |, &, and ~
# Oh wait, duh it's ^
def xor(x,y):
    #return (x | y) & (~(x & y))
    return x ^ y

# Naive solution
def sol1(s, x):
    pairs = []
    for a in range(0,s/2 + 1):
        b = s - a
        if (xor(a, b) == x):
            pairs.append((a,b))
            if a != b:
                pairs.append((b,a))
    return pairs

# Should be rather faster, especially if no solutions (which should happen
# fairly often).
#
# Build a solution from right to left by considering
# the one-digit case first:
# a if s=0 and x=0 then (0,0) solves, and (1,1) if we ignore carries
# b if s=1 and x=0 there is no solution
# c if s=0 and x=1 there is no solution
# d if s=1 and x=1 then (1,0) or (0,1) solves
#
# So given s, x consider first solutions to s0 = s & 1, x0 = x & 1 if any
# if none then there will be no solution for (s,x).
# In case (d)
# let s1,x1 be s,x shifted to the right, call the method for (s1,x1), and for
# each solution (a,b) yield solutions (2*a+1,2*b), (2*a,2*b + 1)
# In case (a)
# For each solution (a,b) yield the solutions (2*a,2*b) but also
# consider solutions for (s1-1, x1) (for the case where there is a carry
# and yield solutions (2*a + 1, 2*b + 1)
def sol2(s, x):
    if (s == 0) and (x == 0):
        return [(0,0)]
    s0 = s & 1
    x0 = x & 1
    sol = []
    if (s0 == 0) and (x0 == 1):
        return sol
    if (s0 == 1) and (x0 == 0):
        return sol
    if (s0 == 1) and (x0 == 1):
        s1 = s / 2
        x1 = x / 2
        pairs = sol2(s1, x1)
        for p in pairs:
           a = p[0]
           b = p[1]
           sol.append((2*a + 1, 2*b    ))
           sol.append((2*a    , 2*b + 1))
        return sol
    if (s0 == 0) and (x0 == 0):
        s1 = s / 2
        x1 = x / 2
        pairs = sol2(s1, x1)
        for p in pairs:
           a = p[0]
           b = p[1]
           sol.append((2*a, 2*b))
        pairs = sol2(s1 - 1, x1)
        for p in pairs:
           a = p[0]
           b = p[1]
           sol.append((2*a + 1, 2*b + 1))
        return sol

def xorTest():
    if xor(0,1) != 1:
        return False
    if xor(1,0) != 1:
        return False
    if xor(1,1) != 0:
        return False
    for i in range(0, 50):
        if xor(i,63) != 63-i:
            print i, 63, 63-i, xor(i, 63)
            return False
        if xor(63, i) != 63 - i:
            print 63, i, 63-i, xor(63, i)
            return False
    if xor(9,5) != 12:
        print 9,5,12,xor(9,5)
        return False
    if xor(11,3) != 8:
        print 11,3, 8, xor(11,3)
        return False
    return True

if __name__ == '__main__':
    print "XOR function test passes: ", xorTest()
    print "Solutions for s=9,x=5: ", sol1(9,5)
    print "Solutions for s=9,x=5: ", sol2(9,5)
    for i in range(0,100):
        for j in range(0,100):
            if len(sol1(i,j)) != len(sol2(i,j)):
                print i, j, "Does not agree"
                print sol1(i,j)
                print sol2(i,j)
    for i in range(0,10):
        s = 101
        sl = sol1(s,2*i)
        if len(sl) != 0:
            print "Error?", sl
