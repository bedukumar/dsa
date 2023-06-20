n = int(input())
l = []
while n > 0:
    w = input()
    l.append(w)
    n -= 1
for i in l:
    if len(i) <= 10:
        print(i)
    else:
        print(i[0]+str(len(i)-2)+i[-1])
