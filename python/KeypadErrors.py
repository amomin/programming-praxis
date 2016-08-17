#!/bin/python
###################### Keypad Errors ##########################
##################### August 02, 2016  #########################
#
# Sometimes one key on a keyboard gets stuck, so some keys that
# are struck do not register. For instance, you may be trying
# to type 18684 on a numeric keypad, but if the 8 key is stuc,
# the keyboard registers you typing 164 instead. Assume the
# only input allowed is the digits 0 through 9.
#
# Your task is to write a program that takes a target number,
# say a PIN, and a keyboard input, and determines if the keyboard
# input matches the target number assuming a single key is stuck.
#
# Note: My interpretation of the problem differed from the statement,
#   but the other interpretation can be recovered by looping
#   over all stuck digits 0-9 - see keypad_errors_any
#
##############################################################

def keypad_errors_any(key_input, pin):
    # Zero characters case
    if keypad_errors(key_input, pin, ""): return True
    for i in range(10):
        if keypad_errors(key_input, pin, i): return True
    return False

def keypad_errors(key_input, pin, stuck):
    i = 0
    j = 0
    while i < len(key_input) and j < len(pin):
        if (key_input[i] == stuck):
            i += 1
            continue
        if (key_input[i] != pin[j]):
            return False
        i += 1
        j += 1
    if i < len(key_input): return False
    if j < len(pin): return False
    return True

if __name__ == '__main__':
    k = "0122345"
    p = "01345"
    s = "2"
    print k, p, s, keypad_errors(k, p, s)
    k = "0122345"
    p = "01345"
    s = "3"
    print k, p, s, keypad_errors(k, p, s)
    k = "0122345"
    p = "012245"
    s = "3"
    print k, p, s, keypad_errors(k, p, s)
