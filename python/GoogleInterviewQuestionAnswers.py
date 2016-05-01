import heapq
import GoogleInterviewQuestion

# Solution g3a from user Paul
def g3a(words):
    word_info = [(-len(w), set(w)) for w in set(words)]
    heapq.heapify(word_info)
    sorted_info = [heapq.heappop(word_info)]
    L = sorted_info[0][0]
    maxlength = 0
    while word_info:
        length2, chars2 = heapq.heappop(word_info)
        if length2 * L <= maxlength:
            break
        for length, chars in sorted_info:
            if length * length2 <= maxlength:
                break
            if not (chars & chars2):
                maxlength = length * length2
        sorted_info.append((length2, chars2))
    return maxlength

def timeMethod(method, wordlist):
   s = time.time()
   ans = method(wordlist)
   return time.time() - s

import random, string, time

def randomWordList(n):
    wordlist = []
    minlen = 3
    for i in range(0,n):
        # Use ascii_lowercase only since g3a distinguishes case
        rword = "".join([random.choice(string.ascii_lowercase) for n in xrange(minlen)])
        r = random.random()
        while r < 0.5:
            rword += random.choice(string.ascii_lowercase)
            r = random.random()
        wordlist.append(rword)
    return wordlist

if __name__ == '__main__':
    print "Checking consistency of g3a and heap..."
    for j in range(0,1000):
        wordlist = randomWordList(20)
        (w1,w2) = GoogleInterviewQuestion.heapSol(wordlist)
        ans1 = len(w1)*len(w2)
        ans2 = g3a(wordlist)
        if  ans1 != ans2:
            print "Fail....", ans1, ans2
            print wordlist
            print w1,w2
            exit(0)
    print "Pass"

    print "Timing g3a vs heapSol"
    time1 = 0
    time2 = 0
    for j in range(0,2):
        wordlist = randomWordList(1000000)
        time1 += timeMethod(GoogleInterviewQuestion.heapSol, wordlist)
        time2 += timeMethod(g3a, wordlist)

    if time1 > time2:
        print "g3a is faster"
    else:
        print "heapSol is faster"

    print "HeapSol: ", time1, ", g3a: ", time2
