def LSA(A,n):
    res,st,i=[],[],0
    while i<n:
        while st and A[st[-1]]>=A[i]:
            st.pop()
        if not st:
            res.append(-1)
        else:
            res.append(st[-1])
        st.append(i)
        i+=1
    return res
def RSA(A,n):
    res,st,i=[],[],n-1
    while i>=0:
        while st and A[st[-1]]>=A[i]:
            st.pop()
        if not st:
            res.append(n)
        else:
            res.append(st[-1])
        st.append(i)
        i-=1
    return res
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    ls=LSA(l,n)
    rs=RSA(l,n)
    rs=rs[::-1]
    # print(ls,rs)
    Area=float('-inf')
    for i in range(n):
    	Area=max(Area,(rs[i]-ls[i]-1)*l[i])
    print(Area)
        
	
