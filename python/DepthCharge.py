#!/usr/bin/python
##################### Depth Charge ###########################
##################### July 05, 2016  #########################
#
# https://programmingpraxis.com/2016/07/05/depth-charge/
#
# In this program, you are the captain of the destroyer, USS 
# Digital. An enemy submarine has been causing trouble and your 
# mission is to destroy it. You may select the size of the "cube"
# of water you wish to search in. The computer then determines 
# how many depth charges you get to destroy the submarine.
# 
# Each depth charge is exploded by you specifying a trio of numbers;
# the first two are the surface coordinates, the third is the 
# depth. After each depth charge, your sonar observer will tell 
# you where the explosion was relative to the submarine.
#
##############################################################

from math import log
from random import randint

def try_hit(charge_x,charge_y,charge_z, try_x, try_y, try_z):
    dx = try_x - charge_x
    dy = try_y - charge_y
    dz = try_z - charge_z
    xdir = "EAST" if dx > 0 else ("WEST" if dx < 0 else "")
    ydir = "NORTH" if dy > 0 else ("SOUTH" if dy < 0 else "")
    zdir = "TOO HIGH" if dz > 0 else ("TOO LOW" if dz < 0 else "DEPTH OK")
    xydir = ydir + xdir
    if (len(xydir) == 0) and (zdir == "DEPTH OK"):
        return ""
    msgstart = ""
    if len(xydir) == 0:
        msgstart = "SONAR REPORTS SHOT WAS"
    else:
        msgstart = "SONAR REPORTS SHOT WAS {0:s} AND".format(xydir)
    return "{0:s} {1:s}".format(msgstart,zdir)

def prompt_charge(message):
    n = raw_input(message)
    n = n.replace(" ","").split(',')
    if (len(n) == 3):
        x,y,z = n
        if x.isdigit() and y.isdigit() and z.isdigit():
            return int(x), int(y), int(z)
    print "Bad input, enter 3 numbers separated by commas"
    return prompt_charge(message)

def prompt_integer(message):
    n = 'a'
    while (not n.isdigit()):
        n = raw_input(message)
    return int(n)

def main():
    n = prompt_integer("DIMENSION OF SEARCH AREA?")
    x,y,z = randint(1, n), randint(1, n), randint(1, n)
    msg = ""
    msg += " \n"
    msg += "YOU ARE CAPTAIN OF THE DESTROYER USS DIGITAL. \n"
    msg += "AN ENEMY SUB HAS BEEN CAUSING YOU TROUBLE. YOUR \n"
    msg += "MISSION IS TO DESTROY IT. YOU HAVE 4 SHOTS. \n"
    msg += "SPECIFY DEPTH CHARGE EXPLOSION POINT WITH A \n"
    msg += "TRIO OF NUMBERS -- THE FIRST TWO ARE THE \n"
    msg += "SURFACE COORDINATES; THE THIRD IS THE DEPTH. \n"
    msg += " \n"
    msg += "GOOD LUCK!"
    msg += " \n"
    ntries = 0
    maxtries = int(log(n, 2)) + 1
    print msg
    while (len(msg) > 0) and ntries < maxtries:
        ntries += 1
        xt, yt, zt = prompt_charge("TRIAL # {0:d} ?".format(ntries))
        msg = try_hit(x,y,z,xt,yt,zt)
        print msg
    if (len(msg) == 0):
        print "B O O M ! !  YOU FOUND IT IN {0:d} TRIES!".format(ntries)
    else:
        print "YOU HAVE BEEN TORPEDOED!  ABANDON SHIP!"
        print "THE SUBMARINE WAS AT {0:d}, {1:d}, {2:d}".format(x,y,z)
    play_again = raw_input("PLAY AGAIN? (Y/N)")
    if play_again == 'Y':
        main()
    else:
        print "OK.  HOPE YOU ENJOYED YOURSELF."

if __name__ == '__main__':
    main()
