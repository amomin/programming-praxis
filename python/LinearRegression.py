#!/usr/bin/python
############################### Linear Regression ###############################
################################# June 10, 2016  ################################
#
# https://programmingpraxis.com/2016/06/10/linear-regression/
#
# Linear regression is a widely-used statistical technique for relating 
# two sets of variables, traditionally called x and y; the goal is to find 
# the line-of-best-fit, y = m x + b, that most closely relates the two 
# sets.  Your task is to write a program that calculates the slope m and 
# intercept b for two sets of variables x and y.
#
#################################################################################

import random
import numpy as np

def linear_regression(x, y):
    n = min(len(x), len(y))
    x = x[0:n]
    y = y[0:n]
    sx = sum(x)
    sy = sum(y)
    sxx = np.dot(x,x)
    sxy = np.dot(x,y)
    m = float(( n* sxy - sx*sy )) / ( n * sxx - sx*sx )
    b = float((sy - m*sx)) / n
    return m, b

if __name__ == '__main__':
    print "Praxis' example: (m,b) = "
    x = [60,61,62,63,65]
    y = [3.1,3.6,3.8,4.0,4.1]
    print linear_regression(x,y)
    print "Test for colinear points (1,4),(2,5),(3,6):"
    x = [1,2,3]
    y = [4,5,6]
    print linear_regression(x,y)
    print "Same dataset, but where len(x) != len(y):"
    x = [1,2]
    y = [4,5,6]
    print linear_regression(x,y)
    x = [1,2,3]
    y = [4,5]
    print linear_regression(x,y)
    print "Random example: (m,b) = "
    x = []
    y = []
    for i in range(0,10):
        x.append(random.randint(1,20))
        y.append(random.randint(1,20))
    print linear_regression(x,y)
