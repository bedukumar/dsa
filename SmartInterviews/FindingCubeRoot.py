for i in range(int(input())):
    n=int(input())
    te=0
    res=0
    if n<0:
        te=abs(n)
    else:
        te=n
    l=1
    h=te
    while(l<=h):
        m=(l+h)//2
        
        if m**3==te:
            print(m) if n>0 else print(m*(-1))
            break
        elif m**3<te:
            l=m+1
        else:
            h=m-1
