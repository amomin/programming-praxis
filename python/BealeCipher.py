# Beale cipher
# Dec 3 2016
# https://programmingpraxis.com/2016/12/02/beales-cipher/

import random

# Programming praxis makes the good point that the appropriate data
# structure for the cipher diphers between the encipher and decipher
# operations.  In the decipher stage a map from  the word index to its
# first letter is desired.  In the decipher stage a map from a character
# to some (random) index of a word starting with that character is desired.  So
# I rewrote the code a little to reflect that.

def word_list(key):
    key = key.lower()
    return key.split()

def make_dict(key):
    keydict = []
    for i in range(26):
        keydict.append([])
    words = word_list(key)
    wordcounter = 0
    for w in words:
        #97 == ord('a')
        i = ord(w[0]) - 97
        keydict[i].append(wordcounter)
        wordcounter += 1
    return keydict

def encipher(key, plain):
    keydict = make_dict(key)

    coded = []
    plain = plain.lower()
    
    for c in plain:
        #97 = ord('a')
        i = ord(c) - 97
        code = 26
        if i > -1 and i < 26:
            d = keydict[i]
            n = len(d)
            r = random.randint(0,n-1)
            code = d[r]
        coded.append(code)
    return coded

def decipher(key, coded):
    plain = ""
    words = word_list(key)
    for i in coded:
        if i > 25:
            plain += " "
        else:
            x = words[i][0]
            plain += x
    return plain

def main():
    ciphered = encipher("Bro's dust e way at moes, Billy.  Oh no.", "Bob and me")
    print ciphered
    deciphered = decipher("Bro's dust e way at moes, Billy.  Oh no.", ciphered)
    print deciphered


if __name__ == '__main__':
    main()
