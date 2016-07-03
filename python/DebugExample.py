# Example on debugging with pdb, vimpdb
#
# See https://github.com/gotcha/vimpdb for more information
# on using vimpdb in particular
#

# Simple function calling pdb to debug
def dbg_pdb():
    import pdb; pdb.set_trace()
    x = 1
    y = 2
    print x + y
    for i in range(0,3):
        print i
    return True

# Simple function calling vimpdb to debug
def dbg_vimpdb():
    import vimpdb; vimpdb.set_trace()
    x = 1
    y = 2
    print x + y
    for i in range(0,3):
        print i
    return True

if __name__ == '__main__':
    n = input("Press 1 to debug in pdb, 2 to debug in vimpdb:")
    if n == 1:
        dbg_pdb()
    if n == 2:
        dbg_vimpdb()
