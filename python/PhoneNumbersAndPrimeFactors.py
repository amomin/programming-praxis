#!/usr/bin/python
####################### Phone Numbers and Prime Factors  #######################
################################ June 24, 2016  ################################
#
# https://programmingpraxis.com/2016/06/24/phone-numbers-and-prime-factors/
#
# Your task is to write a function that determines the number 
# of distinct prime factors of a number, and use that function 
# to explore the distribution of the number of distinct prime 
# factors in a range of telephone numbers.
#
#################################################################################

import math, random, time, pandas as pd

# Equivalent to:
#import NumberTheory
#factor = NumberTheory.factor
def factor(n):
    f=2
    _max = int(math.sqrt(n))+1
    _factors=[]
    while n>1 and f< _max:
        k=0
        while (n%f==0):
            k+=1
            n/=f
        if k>0:
            _factors.append([f,k])
            _max = int(math.sqrt(n))+1
        f+=1
    if n > 1:
        _factors.append([n,1])
    return _factors

def numberOfFactors(n):
    return len(factor(n))

# Analyze number of distince factors in numbers between
# nmin and nmax
def resultsForPhoneNumberRange(nmin, nmax, NSamples=10000):
    _dict = {}
    # We're reporting on statistics, and allowing repitition
    # should not introduce significant bias.
    # So we will just select random numbers in the range.
    for j in range(0,NSamples):
        i = random.randint(nmin,nmax)
        m = numberOfFactors(i)
        if m not in _dict:
            _dict[m] = 0
        _dict[m] += 1
    return _dict

def reportOnRange(_nmin, _nmax, NSamples=10000):
    d = resultsForPhoneNumberRange(_nmin, _nmax, NSamples=NSamples)
    sk = pd.Series(d.keys(), name='Factors')
    sv = pd.Series(d.values(), name='Counts')
    df = pd.concat([sk,sv], axis=1)
    print "Average:"
    print float((sk * sv).sum())/(sv.sum())

    print "Fraction of numbers with 2,3 or 4 factors:"
    print float(d[2] + d[3] + d[4]) / sv.sum()
    print "Fraction of numbers with 3,4 or 5 factors:"
    print float(d[5] + d[3] + d[4]) / sv.sum()
    s = sv / sv.sum()
    print "Histogram:"
    print df

if __name__ == '__main__':
    tic = time.time()
    NSamples = 10000
    print "Analyzing all possible phone numbers using sample of size", NSamples
    reportOnRange(2011000000,9999999999,NSamples=NSamples)
    toc = time.time()
    print "Run time: ", toc - tic
