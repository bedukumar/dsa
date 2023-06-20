x, y = map(int, input().split())
l = list(map(int, input().split()))
c = 0
for i in l:
    if i >= l[y-1] and i > 0:
        c += 1
print(c)
