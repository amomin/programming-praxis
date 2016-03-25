class Boat:
    def __init__(self, k):
        self.seats = [0] * k
        self.k = k

    def fits(self, x):
        return (self.seats[self.k-1] == 0) and (self.weight() + x <= 150)

    def weight(self):
        return sum(self.seats)

    def string(self):
        res = '('
        for x in self.seats:
            res += str(x) + ', '
        return res[:len(res) - 2] + ')'

    def seat(self, x):
        if not self.fits(x):
            raise Exception("Does not fit on boat")
        if not (self.seats[self.k-1] == 0):
            raise Exception("Boat is full")
        i = 0
        while self.seats[i] != 0:
            i += 1
        self.seats[i] = x
            
    def non_empty_seats(self):
        i = 0
        while (i < self.k) and (self.seats[i] != 0):
            i += 1
        return i

    def expand(self, newk):
        if newk < self.k:
            raise Exception("New boat has fewer seats", newk, self.seats)
        newseats = [0] * newk
        for i in range(0,self.k):
            newseats[i] = self.seats[i]
        self.seats = newseats
        self.k = newk
    
    def clone(self):
        b = Boat()
        b.k = self.k
        b.seats = self.seats[:]
        return b

class Boat3(Boat):
    def __init__(self):
        self.k = 3 
        self.seats = [0] * 3

    def clone(self):
        b = Boat3()
        b.seats = self.seats[:]
        return b
