import random

# Problem statement.
#
# You are given two bags, one containing bolts and the other containing nuts, and
# you need to find the biggest bolt.. You may compare bolts to nuts, to see which
# is larger, but you may not compare bolts to bolts or nuts to nuts. Write a
# program to find the biggest bolt.
#
# Comments: Note that the problem is not well-posed: e.g. if the set of 
# nuts is empty, you cannot solve the problem.  There must be at least one nut
# which the largest bolt will not fit.  This program will only find a solution
# if that is the case, though it will always return a candidate solution.


def nuts_and_bolts(nuts, bolts):
    size = len(nuts)
    biggest = -1
    for b in bolts:
        nuts = filter(lambda x: x >= b, nuts)
        new_size = len(nuts)
        if new_size < size:
            size = new_size
            biggest = b
    return biggest

def main():
    nuts = []
    bolts = []
    for i in range(20):
        nuts.append(random.random())
    for i in range(5):
        bolts.append(random.random())
    print "Nuts: ", nuts
    print "Bolts: ", bolts
    print nuts_and_bolts(nuts, bolts)

if __name__ == '__main__':
    main()
