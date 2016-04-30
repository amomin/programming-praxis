#!/usr/bin/python

# Increment a pandigital number
def incr(pandigital):
    # Start from the right.  Go left until you find a digit
    # which is smaller than some previous digit seen.  Replace it
    # with the smallest digit to its right, and replace the digits
    # to the right with the sorted list of the digits so far encountered
    dl = to_digitlist(pandigital/10)
    cnt = len(dl) - 1
    maxsofar = dl[cnt]
    while dl[cnt] >= maxsofar:
        maxsofar = dl[cnt]
        cnt -= 1
    # Some digit to the right is larger.  Replace
    # with the least digit to the right, and then
    # reorder digits to the right in ascending order
    rest = dl[cnt + 1:]
    curr = dl[cnt]
    minlarger = min( filter (lambda x: x > curr, rest) )
    rest = filter(lambda x: x != minlarger, rest)
    rest.append(curr)
    rest.sort()
    dl = dl[:cnt] + [minlarger] + rest 
    return from_digitlist(dl)

# Decremet a pandigital number
def decr(pandigital):
    # Flip the digits (1->9, 2->8, etc...) and use increment,
    # then flip back
    dl = to_digitlist(pandigital/10)
    dl = map(lambda x: 10 - x, dl)
    rev = from_digitlist(dl)
    rev = incr(rev)
    dl = to_digitlist(rev/10)
    dl = map(lambda x: 10 - x, dl)
    return from_digitlist(dl)

def to_digitlist(num):
    return map(lambda x: int(x), str(num))

def from_digitlist(dl):
    return int(''.join(map(str,dl))) * 10

def smallestSol1():
    # Divisibility by 9 is automatic.
    # Divisibility by 2,5 implies that the last digit
    # must be zero.  Divisibility by 8 is equivalent to
    # the last three digits must be divisible by 8, and becaus
    # of 5, in fact must be divisible by 40.
    # I don't have a rule for divisibility by 7
    pd = 1234567890
    sol = []
    while len(sol) < 2:
        cond = (pd % 7 == 0) and (pd % 40 == 0)
        if cond:
            sol.append(pd)
        pd = incr(pd)
    return sol

def largestSol1():
    # Divisibility by 9 is automatic.
    # Divisibility by 2,5 implies that the last digit
    # must be zero.  Divisibility by 8 is equivalent to
    # the last three digits must be divisible by 8, and becaus
    # of 5, in fact must be divisible by 40.
    # I don't have a rule for divisibility by 7
    pd = 9876543210
    sol = []
    while len(sol) < 2:
        cond = (pd % 7 == 0) and (pd % 40 == 0)
        if cond:
            sol.append(pd)
        pd = decr(pd)
    return sol

def test_incr():
    pd = 1234567890
    for i in range(0,100):
        print pd
        pd = incr(pd)
def test_decr():
    pd = 9876543210
    for i in range(0,10):
        print pd
        pd = decr(pd)

if __name__ == '__main__':
    #test_incr()
    #test_decr()
    print smallestSol1()
    print largestSol1()
