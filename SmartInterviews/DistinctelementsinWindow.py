for _ in range(int(input())):
    x,k=map(int,input().split())
    l=list(map(int,input().split()))
    d={}
    i=0
    while i<=k-2:
        if l[i] in d:
            d[l[i]]+=1
        else:
            d[l[i]]=1
        i+=1
    i-=1
    j=-1
    while i<x-1:
        i+=1
        if l[i] not in d:
            d[l[i]]=1
        else:
            d[l[i]]+=1
        # print(d)
        print(len(d),end=" ")
        j+=1
        if l[j] in d and d[l[j]]==1:
            d.pop(l[j])
        elif l[j] in d:
            d[l[j]]-=1
    print()
            
            
            
            
            
            
