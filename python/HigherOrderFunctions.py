

#
# Trivial implementation is
# def stringMap( proc, strng):
#   return "".join(map(proc, string))
#
def stringMap( proc, strng ):
    res = "";
    for x in range(0,len(strng)):
       res += proc(strng[x]) #Recommended way apparently
    return res

#
# Trivial implementation is
# def stringForEach( proc, strng):
#   map( proc, strng)
#
def stringForEach( proc, strng ):
    for x in range(0,len(strng)):
        proc(strng[x])

#
# Trivial implementation is
# def stringFold( proc, strng):
#   reduce( proc, strng, base)
def stringFold( proc, base, strng ):
    acc = base
    if len(strng) < 1:
        return acc
    for x in range(0,len(strng)):
        acc = proc(acc, strng[x])
    return acc
