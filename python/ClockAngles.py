#!/usr/bin/python
################################ Clock Angles  ################################
################################ July 01, 2016  ###############################
#
# https://programmingpraxis.com/2016/07/01/clock-angles/
#
# Write a program that, given a time as hours and minutes (using 
# a 12-hour clock), calculates the angle between the two hands. For
# instance, at 2:00 the angle is 60 degrees.
#
#################################################################################

# The hour hand moves 1 degree every 2 minutes
def hour_angle(h,m):
    h = h % 12
    m = m % 60
    return (float(60 * h + m) / 2) % 360

# The minute hand moves 6 degrees per minute
def minute_angle(m):
    m = m % 60
    return float(6 * m) % 360

def angle_difference(a1, a2):
    pos_diff = a1 - a2 if (a1 > a2) else a2 - a1
    diff = pos_diff if (pos_diff < 180) else 360 - pos_diff
    return diff

def hand_difference(h, m):
    a1 = hour_angle(h, m)
    a2 = minute_angle(m)
    return angle_difference(a1, a2)

from math import floor

if __name__ == '__main__':
    print "On the hour:"
    for i in range(0,12):
        print "At {0:02d}:00 - ".format(i), hand_difference(i,0)

    print "On the half-hour:"
    for i in range(0,12):
        print "At {0:02d}:30 - ".format(i), hand_difference(i,30)

    print "At quarter after:"
    for i in range(0,12):
        print "At {0:02d}:15 - ".format(i), hand_difference(i,15)

    print "At quarter to:"
    for i in range(0,12):
        print "At {0:02d}:45 - ".format(i), hand_difference(i,45)

    print "At times where the angle should be zero:"
    for i in range(0,11):
        h = i
        # (60h + m)/2 = 6m
        # 60h = 11m
        # m = 60h/11
        m = float(60 * h) / 11
        s = int(float(m % 1) * 60)
        print "At {0:02d}:{1:02.0f}:{2:02d} - {3:.05f} degrees".format(h,floor(m),s,hand_difference(h,m))
