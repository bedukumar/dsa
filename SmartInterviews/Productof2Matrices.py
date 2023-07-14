t=int(input())
while t>0:
    r,c=map(int,input().split())
    l=[]
    for i in range(r):
        l.append(list(map(int,input().split())))
    x,y=map(int,input().split())
    k=[]
    for i in range(x):
        k.append(list(map(int,input().split())))
    if c == x:
        z=[[ 0 for _ in range(y) ] for x in range(r)]
        for i in range(r):
            for j in range(y):
                for _ in range(c):
                    z[i][j]+=l[i][_]*k[_][j]
        for _ in z:
            print(*_)
                    
    t-=1
