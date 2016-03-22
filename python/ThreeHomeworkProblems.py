def sum1(xs):
   return sum(xs) 

def sum2(xs):
    if len(xs) == 0:
        return 0
    return xs[0] + sum2(xs)

def rev0(xs):
    xs.reverse()
    return xs

def rev1(xs):
    if len(xs) == 0:
        return []
    return rev1(xs[1:]) + [xs[0]]

def isort(xs):
    def ins(t, ys):
        if len(ys) == 0:
            return [t]
        else:
            if t < ys[0]:
                return [t] + ys
            else:
                return [ys[0]] + ins(t, ys[1:])
    def hlp(xs, prefix):
        if len(xs) == 0:
            return prefix
        x = xs[0]
        t = xs[1:]
        return hlp(t, ins(x, prefix))
    return hlp(xs, [])
                
