# Dollar Format
# September 30, 2016
# https://programmingpraxis.com/2016/09/30/dollar-format/

def dollar_format(n):
    # Method 1: potentially buggy due to behavior of round
    # round(2.675,2)=2.67 rather than 2.68
    # cents =int(round((n%1)*100)) 
    # Method 2: We will actually look at the 3rd character after the decimal
    cents = int(round((n%1)*1000))
    if cents % 10 < 5:
        cents = cents/10
    else:
        cents = cents/10 + 1
    
    # If cents rounds up to 100 e.g. .995 dollars, then we
    # need to carry over into the dollar amount
    carry = 0
    if cents == 100:
        cents = 0
        carry = 1

    # Need to take care to pad zeros correctly
    # Not only here, but also while building the thousands string
    s=str(cents)
    if len(s)<2:
        s="0"+s
    s="."+s
    n = int(n) + carry
    if n == 0:
        return '$0'+s
    while n > 0:
        # Pad with zeros if necessary
        a = str(n % 1000)
        if len(a) == 1: a ="00"+a
        if len(a) == 2: a ="0" +a
        s = "," + a + s
        n /= 1000
    s=s[1:]
    while s[0]=="0":
        s=s[1:]
    return '$' + s

if __name__ == '__main__':
    n = 0
    print n, "->",dollar_format(n)
    n = 0.99
    print n, "->",dollar_format(n)
    n = 0.01
    print n, "->",dollar_format(n)
    n = 0.09
    print n, "->",dollar_format(n)
    n = 1.675
    print n, "->",dollar_format(n)
    print "Potential bug due to suprising (but not incorrect) behavior of python round()"
    n = 2.675
    print n, "->",dollar_format(n)
    n = 999.995
    print n, "->",dollar_format(n)
    n = 1000.01
    print n, "->",dollar_format(n)
    n = 1000
    print n, "->",dollar_format(n)
    n = 123243.1243
    print n, "->",dollar_format(n)
    n = 9234271231234.765123123
    print n, "->",dollar_format(n)
