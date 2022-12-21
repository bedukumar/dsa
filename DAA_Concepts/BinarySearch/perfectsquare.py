def isPerfect(n):
    l, r = 1, n
    while l <= r:
        mid = (l+r)//2
        if mid*mid > n:
            r = mid-1
        elif mid*mid < n:
            l = mid+1
        else:
            return True
    return False


print(isPerfect(15))
