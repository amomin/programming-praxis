#!/usr/bin/python
########################### Two Interview Questions ###########################
################################ June 21, 2016  ################################
#
# https://programmingpraxis.com/2016/06/21/two-interview-questions-2/
#
# Given a function rand2 that returns 0 or 1 with equal probability, 
# write a function rand3 that returns 0, 1 or 2 with equal probability, 
# using only rand2 as a source of random numbers.
#
# Given a set of characters and a dictionary of words, find the shortest word 
# in the dictionary that contains all of the characters in the set.
# In case of a tie, return all the words of the same (shortest) length.
#
#################################################################################

import math, random

def rand2():
    return int(round(random.random()))

def rand3():
    tosses = map(lambda x: rand2(), [0] * 3)
    heads = len(filter(lambda x: x == 1, tosses))
    if (heads == 0) or (heads == 3):
        return rand3()
    elif (heads == 1):
        for i,x in enumerate(tosses):
            if x == 1: return i
    else: # two tails (0s)
        for i,x in enumerate(tosses):
            if x == 0: return i
    return int(math.round(random.random()))

##
# Find the shortest word(s) in dictionary that contain all the characters of
# the given word.  This method does not consider multiplicity.
##
def dict_match(word, dictionary):
    # Just run through the dictionary
    N = len(dictionary)
    if N < 1: return []
    sortedwordset = set(word)
    matches = []
    # Oh no, running through twice, but otherwise not sure how
    # to guarantee maxlengh is large enough
    maxlength = max(map(len, dictionary))
    # Oh, could use maxlength = float("inf")
    i = 0
    while i < N:
        if sortedwordset < set(dictionary[i]):
            l = len(dictionary[i])
            if l == maxlength:
                matches.push(dictionary[i])
            elif l < maxlength:
                matches = [dictionary[i]]
                maxlength = l
        i+= 1
    return matches

# Assumes lower case!!!
def _word_vector(word):
    #97 = ord('a')
    return map(lambda c: len(filter(lambda x: x == chr(97 + c), word)), range(0,26))

# Returns true if an only if each letter appears in "word" at least as many times
# as it appears in "candidate". i.e. "candidate" is subword of "word"
# Assumes lower case!!! see _word_vector
def _is_subword_of(word, candidate):
    wv = _word_vector(word)
    cv = _word_vector(candidate)
    N = len(wv)
    for i in range(0,N):
        if wv[i] < cv[i]:
            return False
    return True

##
# Find the shortest word(s) in dictionary that contain all the characters of
# the given word.  This method each letter must appear at least as many times as
# in the given word.
#
# Assumes lower case!!!
#
##
def dict_match2(word, dictionary):
    # Just run through the dictionary
    N = len(dictionary)
    if N == 0:
        return []
    matches = []
    # Oh no, running through twice, but otherwise not sure how
    # to guarantee maxlengh is large enough
    maxlength = max(map(len, dictionary))
    i = 0
    while i < N:
        if _is_subword_of(dictionary[i], word):
            l = len(dictionary[i])
            if  l == maxlength:
                matches.push(dictionary[i])
            elif l < maxlength:
                matches = [dictionary[i]]
                maxlength = l
        i+= 1
    return matches

if __name__ == '__main__':
    N = 100000
    count = {0:0,1:0,2:0}
    for i in range(0,N):
        count[rand3()] += 1
    print "Result of", N, "coin rand3() calls:"
    print count

    word = "apples"
    dictionary = []
    print dict_match(word, dictionary), "=", word, dictionary

    word = "apples"
    dictionary = ["baby", "blue", "app", "staples", "papless", "applesauce"]
    print dict_match(word, dictionary), "=", word, dictionary
   
    word = "apples"
    dictionary = ["baby", "blue", "app", "staples", "papless", "applesauce"]
    print dict_match2(word, dictionary), "=", word, dictionary
