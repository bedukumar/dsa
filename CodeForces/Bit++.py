n = int(input())
l = [input() for i in range(n)]
c = 0
for i in l:
    if i == "X++" or i == "++X":
        c += 1
    if i == "--X" or i == "X--":
        c -= 1
print(c)
