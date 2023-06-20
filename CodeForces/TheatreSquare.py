import math as m
x, y, z = map(int, input().split())
print(m.ceil(x/z)*m.ceil(y/z))
