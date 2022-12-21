def squareRoot(n):
    e = 0.000001
    l, r = 1, n
    while r-l > e:
        m = (r+l)/2
        if m*m < n:
            l = m
        else:
            r = m
    return l


print("%f " % (squareRoot(4)))
