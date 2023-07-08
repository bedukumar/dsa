import sys

for line in sys.stdin:
    t = int(line)
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        sum = 0
        for i in range(n):
            sum = sum ^ (2 * arr[i])
        print(sum)
