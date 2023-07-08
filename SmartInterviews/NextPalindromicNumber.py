import math as m
def nextPalindrome(n):
    ns=str(n)
    l=len(ns)
    if l%2==0:
        ns=ns[:l//2]+ns[:l//2][::-1]
        return int(ns)
    else:
        ns=ns[:l//2]+ns[l//2]+ns[:l//2][::-1]
        return int(ns)
    
t=int(input())
while t>0:
    n=int(input())
    pn=nextPalindrome(n)
    if n<pn:
        print(pn)
    else:
        x=(10**((m.ceil(m.log(pn,10)))//2))
        pn=int(((pn/x)+1)*x)
        pn=nextPalindrome(pn)
        print(pn)
    t-=1
