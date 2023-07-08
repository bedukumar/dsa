t=int(input())
while t>0:
    x,y=map(int,input().split())
    l=list(map(int,input().split()))
    a,b=0,0
    l.sort()
    f=0
    while a<x and b<x:
        d=(l[b]-l[a])
        if d>y:
            a+=1
        if d<y:
            b+=1
        elif d==y and a!=b:
            print("true")
            f=1
            break
    if f==0:
    	print("false")
    t-=1
