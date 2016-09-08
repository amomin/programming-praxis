#!/usr/bin/python
############################### Circular Arrays  ##############################
##############################  August 26, 2016  ##############################
#
# https://programmingpraxis.com/2016/08/26/circular-arrays/
#
# Today's exercise is to write a program that provides queues using a circular
# array. You should provide operations to make a new queue with a user-specified
# maximum size, determine if a queue is empty, add new elements to the end of the
# queue, and remove elements from the beginning of the queue.
#
# Your task is to implement a queue as described above.
#
#################################################################################

class CircularArray:
    arr = []
    head = 0
    tail = 0
    capacity = 0

    def __init__(self, n):
        self.arr = [0]*(n+1)
        self.capacity = n+1

    def size(self):
        return (capacity + tail - head) % capacity

    def add(self, k):
        if (self.capacity + self.head - self.tail) % self.capacity == 1:
            return False
        self.arr[self.tail] = k
        self.tail = (self.tail + 1) % self.capacity
        #print self.tail, self.arr
        return True

    def peek(self):
        if self.head == self.tail:
            return False
        return self.arr[self.head]

    def remove(self):
        if self.head == self.tail:
            return False
        # Clear the value, not necessary but
        # may be useful for debugging
        self.arr[self.head % self.capacity] = 0
        self.head = self.head + 1 % self.capacity
        return True

    def __str__(self):
        s = ""
        i = self.head
        while i % self.capacity != self.tail % self.capacity:
            s += (str(self.arr[i % self.capacity]) + ",")
            i = (i + 1) % self.capacity
        return s

if __name__ == '__main__':
    cq = CircularArray(5)
    cq.add(1)
    cq.add(2)
    cq.add(3)
    cq.add(4)
    print cq
    print cq.peek()
    cq.remove()
    print cq.peek()
    cq.remove()
    cq.add(5)
    cq.add(6)
    print cq
    print cq.peek()
    cq.remove()
    print cq.peek()
    cq.remove()
    print cq
    cq.add(7)
    cq.add(8)
    cq.add(9)
    cq.add(10)
    cq.add(11)
    cq.add(12)
    print cq
    cq.remove()
    cq.remove()
    cq.add(13)
    cq.add(14)
    cq.add(15)
    cq.add(16)
    print cq
    cq.remove()
    cq.remove()
    cq.add(17)
    print cq
