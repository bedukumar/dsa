t=int(input())
d=1
while t>0:
    n=int(input())
    res=[]
    def X(o,c,s):
        if len(s) == n*2 :
            res.append(s)
            return
        if o<n:
            X(o+1,c,s+"{")
        if c<o:
            X(o,c+1,s+"}")
    X(0,0,"")
    print(f"Test Case #{d}:")
    d+=1
    for i in res:
        print(i)
    t-=1
