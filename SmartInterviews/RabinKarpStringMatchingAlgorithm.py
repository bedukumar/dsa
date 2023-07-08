for _ in range(int(input())):
    a,b=input().split()
    k=len(a)
    c=0
    for i in range(len(b)-k+1):
        s=b[i:i+k]
        if s==a:
            c+=1
    print(c)
