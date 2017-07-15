import random

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
