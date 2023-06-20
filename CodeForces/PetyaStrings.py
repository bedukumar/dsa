x = input().lower()
y = input().lower()
c = 0
for i in range(len(x)):
    if ord(x[i]) > ord(y[i]):
        print("1")
        c += 1
        break
    if ord(x[i]) < ord(y[i]):
        print("-1")
        c += 1
        break
    if ord(x[i]) == ord(y[i]):
        continue
if c == 0:
    print("0")
