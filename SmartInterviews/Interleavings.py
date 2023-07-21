res=[]
def printIlsRecur(str1, str2, iStr, m, n, i):
    if m==0 and n==0:
        res.append("".join(iStr))
    if m != 0:
        iStr[i] = str1[0]
        printIlsRecur(str1[1:], str2, iStr, m-1, n, i+1)
    if n != 0:
        iStr[i] = str2[0]
        printIlsRecur(str1, str2[1:], iStr, m, n-1, i+1)
 
def printIls(str1, str2, m, n):
    iStr = [''] * (m+n)
    printIlsRecur(str1, str2, iStr, m, n, 0)
t=int(input())
x=1
while t>0:
    a=input().split()
    print(f"Case #{x}:")
    x+=1
    printIls(a[0],a[1],len(a[0]),len(a[1]))
    res.sort()
    for i in res:
        print(i)
    res=[]
    t-=1
