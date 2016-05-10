################# Concatenate N N Times #####################
##################### May 10, 2016  #########################
#
# https://programmingpraxis.com/2016/05/10/concatenate-n-n-times/
#
# Your task is to write a program that calculates the number
# that is concatenated to itself the number of times as the
# number is (that's hard to say).
# e.g. 7777777
# e.g. 121212121212121212121212
#
##############################################################

def sol1(N):
    ans = ""
    for i in range(0,N):
        ans = ans + str(N)
    return ans

# Using base 2 rep of N to build it in log many steps
# (but still concatenating long strings so maybe not as efficient as may seem)

def repeatStrNTimes(_str, N):
    if N < 0:
        "ERROR"
    if N < 1:
        return ""
    prev = repeatStrNTimes(_str, (N >> 1))
    if (N % 2 == 1):
        return prev + prev + _str
    else:
        return prev + prev

def sol2(N):
    return repeatStrNTimes(str(N), N)

def test1():
    if "" == sol1(0):
        print "Passes on input 0"
    else:
        print "Fails on input 0"
    if "1" == sol1(1):
        print "Passes on input 1"
    else:
        print "Fails on input 1"
    if "88888888" == sol1(8):
        print "Passes on input 8"
    else:
        print "Fails on input 8"
    if "1111111111111111111111" == sol1(11):
        print "Passes on input 11"
    else:
        print "Fails on input 11"
    if "121212121212121212121212" == sol1(12):
        print "Passes on input 12"
    else:
        print "Fails on input 12"
    ten123 = "123123123123123123123123123123"
    hundred123 = ten123 + ten123 + ten123 + ten123 + ten123 + ten123 + ten123 + ten123 + ten123 + ten123
    ans123 = hundred123 + ten123 + ten123 + "123123123"
    if ans123 == sol1(123):
        print "Passes on input 123"
    else:
        print "Fails on input 123"

def test2():
    if "" == sol2(0):
        print "Passes on input 0"
    else:
        print "Fails on input 0"
    if "1" == sol2(1):
        print "Passes on input 1"
    else:
        print "Fails on input 1"
    if "88888888" == sol2(8):
        print "Passes on input 8"
    else:
        print "Fails on input 8"
    if "1111111111111111111111" == sol2(11):
        print "Passes on input 11"
    else:
        print "Fails on input 11"
    if "121212121212121212121212" == sol2(12):
        print "Passes on input 12"
    else:
        print "Fails on input 12"
    ten123 = "123123123123123123123123123123"
    hundred123 = ten123 + ten123 + ten123 + ten123 + ten123 + ten123 + ten123 + ten123 + ten123 + ten123
    ans123 = hundred123 + ten123 + ten123 + "123123123"
    if ans123 == sol2(123):
        print "Passes on input 123"
    else:
        print "Fails on input 123"

if __name__ == '__main__':
    print "Some Tests for sol1:"
    test1()
    print "Some Tests for sol2:"
    test2()
    print "Examples of sol1"
    for i in range(0,20):
        print "Output for N=", i, "is", sol1(i)
    print "Examples of sol2"
    for i in range(0,20):
        print "Output for N=", i, "is", sol2(i)
