t=int(input())
while t>0:
    n=int(input())
    count=0
    while(n >= 5):
        n //= 5
        count += n
    print(count)
    t-=1
