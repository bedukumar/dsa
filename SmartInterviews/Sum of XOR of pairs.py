for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=0
    for i in range(32):
        c=0
        for j in range(0,n):
            if l[j]&(1<<i)!=0:
                c+=1
        pair=c*(n-c)
        s+=2*pair*(1<<i)
    print(s)
    
