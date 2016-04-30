############################ Google Interview Question #############################
#
# April 8, 2016
#
# Given a list of words, find the maximum value of the product of the lengths 
# of two words from the list, subject to the constraint that the two words 
# cannot share any letters. For instance, given the words ABCW, BAZ, FOO
# , BAR, XTFN, and ABCDEF, the pair FOO BAR has a product of 9, the pair 
# BAZ XFTN has a product of 12, and the pair ABCW XTFN has a product of 
# 16, which is the maximum. Note that the pair ABCW ABCDEF doesn't work
# because the two words share three letters.
#
####################################################################################

import heapq

## Obvious solution, run through pairs and compute
def naiveSol(words):
    maxpair = ()
    maxprod = 0
    N = len(words)
    _loopcount = 0
    for i in range(0,N):
        for j in range(i+1,N):
            _loopcount += 1
            a = words[i].lower()
            b = words[j].lower()
            if len(set(a).intersection(b)) == 0:
                n = len(a) * len(b)
                if n > maxprod:
                    maxprod = n
                    maxpair = (words[i], words[j])
    #print "Brute", _loopcount
    return maxpair

# Order the words in descending length, and then return on the first
# match.  Whoops that won't work!  But there must be some improvement along these
# lines.  Leaving this incorrect algorithm for now as a reminder.
def wrongSol(words):
    words.sort(lambda x, y: 1 if len(x) < len(y) else -1) 
    N = len(words)
    for i in range(0,N):
        for j in range(i+1,N):
            a = words[i].lower()
            b = words[j].lower()
            if len(set(a).intersection(b)) == 0:
                return (words[i], words[j])
    return ()

# Work through the list in an order of descending product. One way to do this
# would be to keep a queue of pairs to check after (i,j); namely, start
# with an empty queue, enter the pair (0,1), and on checking the pair (i,j) 
# add (i+1,j) and (i,j+1) to the queue in the correct order.  Stop when a match
# is found.  You can keep a hash table of i,j that have already been checked
# to reduce redundancy, although this adds a space overhead.  The first pair 
# encountered without a collision will be the answer.
#
# MUCH faster than naive solution, even without the checked hashtable
def heapSol(words):
    words.sort(lambda x, y: 1 if len(x) < len(y) else -1)
    checked = {}
    h = []
    N = len(words)
    heapq.heappush(h, (0, (0,1)))
    _loopcount = 0
    while len(h) > 0:
        _loopcount += 1
        (p, (i, j)) = heapq.heappop(h)
        a = words[i].lower()
        b = words[j].lower()
        if len(set(a).intersection(b)) == 0:
            #print "Heap", _loopcount
            return (words[i], words[j])
        if (i + 1 < j) and ((i+1,j) not in checked):
            alen = len(words[i+1])
            blen = len(words[j])
            heapq.heappush(h, (-alen*blen, (i+1,j)))
            checked[(i+1,j)] = True
        if j + 1 < N and ((i,j+1) not in checked):
            alen = len(words[i])
            blen = len(words[j+1])
            heapq.heappush(h, (-alen*blen, (i,j + 1)))
            checked[(i,j+1)] = True
    #print "Heap", _loopcount
    return ()

import random, string, time

def timeMethod(method, wordlist):
   s = time.time()
   (w1, w2) = method(wordlist)
   print "Answer for method ", method.__name__, ": ", len(w1)*len(w2), (w1,w2)
   print("--- %s seconds ---" % (time.time() - s))

if __name__ == '__main__':
    # Sanity check
    #print naiveSol(["a", "mjhdefzef", "Major", "Tom", "bamboo","When", "woman"])
    #print wrongSol(["a", "mjhdefzf", "Major", "Tom", "bamboo","When", "woman"])
    #print heapSol(["a", "mjhdefzef", "Major", "Tom", "bamboo","When", "woman"])

    Nwords = 1000
    n = raw_input('Enter a number')
    Nwords = int(n)
    check_brute = raw_input('Check brute force solution - slow for n > 2000 - Y for yes')
    minlen = 3
    wordlist = []
    print "Generatign a list of words of length ", n
    for i in range(0,Nwords):
        rword = "".join([random.choice(string.ascii_letters) for n in xrange(minlen)])
        r = random.random()
        while r < 0.5:
            rword += random.choice(string.ascii_letters)
            r = random.random()
        wordlist.append(rword)

    print "Running methods..."
    if check_brute == 'Y':
        timeMethod(naiveSol, wordlist)
    timeMethod(wrongSol, wordlist)
    timeMethod(heapSol, wordlist)
