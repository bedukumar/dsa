t=int(input())
while t>0:
    xbl1,ybl1,xtr1,ytr1=map(int,input().split())
    xbl2,ybl2,xtr2,ytr2=map(int,input().split())
    l1=abs(ytr1-ybl1)
    b1=abs(xtr1-xbl1)
    l2=abs(ytr2-ybl2)
    b2=abs(xtr2-xbl2)
    x=(min(xtr1,xtr2)-max(xbl2,xbl1))
    y=(min(ytr1,ytr2)-max(ybl1,ybl2))
    a=0
    if x>0 and y>0:
        a=x*y
    print((l1*b1)+(l2*b2)-a)
    t-=1
