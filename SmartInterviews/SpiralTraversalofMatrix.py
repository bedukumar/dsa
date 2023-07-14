t=int(input())
while t>0:
    n=int(input())
    l=[]
    for i in range(n):
        l.append(list(input().split()))
    k=0
    while k<=n//2:
        i=k
        j=k
        while j<n-k:
            print(l[i][j],end=" ")
            j+=1
        j-=1
        i+=1
        while i<n-k:
            print(l[i][j],end=" ")
            i+=1
        i-=1
        j-=1
        while j>k:
            print(l[i][j],end=" ")
            j-=1
        while i>k:
            print(l[i][j],end=" ")
            i-=1
        i+=1 
        k+=1
    print()
    t-=1
