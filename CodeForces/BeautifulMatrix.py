l = [input().split() for i in range(5)]
x, y = 0, 0
for i in range(5):
    for j in range(5):
        if l[i][j] == '1':
            x, y = i, j
            break
print(abs(3-(x+1))+abs(3-(y+1)))
