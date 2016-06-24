import random

# Make an sample of N integers (without replacement) in
# the range [nmin,nmax].
def makeIntSample(N, nmin, nmax):
    diff = nmax - nmin
    if N >= diff:
        raise Exception("Cannot produce sample of this size in this range")
    sample = []
    if 3*N > diff:
        # Use a swapping strategy
        sample = range(nmin, nmax + 1)
        i = 0
        while i < N:
            x = random.randint(i,diff + 1)
            tmp = sample[i]
            sample[i] = sample[x]
            sample[x] = tmp
            i += 1
    else:
        # Select randomly from available values
        d =  {}
        while (len(d) < N):
            i = random.randint(nmin,nmax)
            if i not in d:
                d[i] = True
        sample = d.keys()
    return sample

