def bs(a, n):
    l = 0
    r = len(a)
    while (l <= r):
        mid = l+(r-l)//2  # mid=(l+r)//2
        if n == a[mid]:
            return l
        elif n > a[mid]:
            l = mid+1
        else:
            r = mid-1

    return l


l = [1, 3, 5, 6, 7]
print(bs(l, 4))
