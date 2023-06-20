l = list(map(int, input().split("+")))
l.sort()
for i in range(len(l)-1):
    print(str(l[i])+"+", end="")
print(l[-1])
