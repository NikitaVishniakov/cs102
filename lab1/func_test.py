def multiplicative_inverse(e, phi):
    """
    Euclid's extended algorithm for finding the multiplicative inverse of two numbers.

    >>> multiplicative_inverse(7, 40)
    23
    """
def multiplicative_inverse(e, phi):
    """
    Euclid's extended algorithm for finding the multiplicative inverse of two numbers.

    >>> multiplicative_inverse(7, 40)
    23
    """
    a = []
    b = []
    c = []
    d = []
    i = 0
    a.append(phi)
    b.append(e)
    c.append(a[i] % b[i])
    d.append(a[i] // b[i])
    while c[i] != 0:
        i += 1
        a.append(b[i-1])
        b.append(a[i-1] % b[i-1])
        c.append(b[i-1] % (a[i-1] % b[i-1]))   
        print( a[i], b[i], c[i])
    s = []
    s.append(a[::-1])
    s.append(b[::-1])
    s.append(c[::-1])
    x, y = [0], [1] 
    s.append(x)
    s.append(y)
    print (s)
    for i in range(0,len(s)):
        s[3].append(s[4][i])
        s[4].append(s[3][i] - s[3][i] * (s[0][i] // s[1][i]))
    d = s[4][len(s)] % s[0][0];
    return d
            
            
#
#        
#multiplicative_inverse(7, 40) 