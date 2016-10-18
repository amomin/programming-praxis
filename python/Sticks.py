"""Sticks - October 7 2016
https://programmingpraxis.com/2016/10/07/sticks/
"""

import heapq

# a,b,c,d
# Greedy if a<b<c<d
# a+b,a+b+c,a+b+c+d
# Another
# a+b,c+d,a+b+c+d
# 3(a+b)+2c+d vs 2(a+b+c+d)
# a+b vs d
# So greedy isn't the answer bc d might be < a+b
# OK Gave up and looked
# Use a heap - combine the two smallest sticks
# So yeah, it's a greedy solution after all...

def sticks(stick_lengths):
    """Solution"""
    heapq.heapify(stick_lengths)
    cost = 0
    while len(stick_lengths) > 1:
        stick1 = heapq.heappop(stick_lengths)
        stick2 = heapq.heappop(stick_lengths)
        cost += stick1+stick2
        print "Combining", stick1, stick2
        heapq.heappush(stick_lengths, stick1+stick2)
    return cost

def test():
    """Demo"""
    sticks_lengths = [1, 2, 4]
    cost = sticks(sticks_lengths)
    print "Cost was", cost

    sticks_lengths = [1, 2, 3, 4]
    cost = sticks(sticks_lengths)
    print "Cost was", cost

    sticks_lengths = [101, 102, 103, 104]
    cost = sticks(sticks_lengths)
    print "Cost was", cost

if __name__ == '__main__':
    test()
