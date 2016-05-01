######################## Interview Timing ############################
######################### April 19, 2016  ############################
#
# https://programmingpraxis.com/2016/04/19/interview-timing/
#
# I came across an interesting interview question recently. I'll 
# tell you the question shortly. What made it interesting was 
# that the same question was given to all candidates, and they 
# were timed in getting a solution; candidates with shorter times 
# were given higher scores than candidates with longer times. 
# 
# Write a program that, given a positive integer n, determines
# if n is a power of two.
#
######################################################################

# I read the question and forgot to start the time, but it
# coudln't have taken much more than a minute, if even a minute.
# I did about half the solution plus the test in just under 
# a minute.

def isPowerOf2(n):
    m = 1
    while m <= n:
        if m == n:
            return True
        else:
            m *= 2
    return False

if __name__ == '__main__':
    for n in range(0,100):
        print n, isPowerOf2(n)

# Naturally, there are better approaches (check how many non-zero
# bits there are in the binary representation, or as programming
# praxis did it check if the number is 1 % 2 and return false 
# - unless the number is 1 - and otherwise divide by two and
# repeat) which are almost always faster but only matters if
# you are doing a large number of these or on exteremely large
# numbers.
