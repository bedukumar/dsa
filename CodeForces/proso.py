n = int(input())
l = []
while n > 0:
    l.append(input().split())
    n -= 1
c = 0
for i in range(len(l)):
    x = 0
    for j in range(len(l[0])):
        if l[i][j] == '1':
            x += 1
    if x >= 2:
        c += 1
print(c)
