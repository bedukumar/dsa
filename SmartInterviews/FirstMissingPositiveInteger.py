for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = set()
    for i in a:
        if i >= 1 and i <= n and i not in s:
            s.add(i)
    for i in range(1, n+1):
        if i not in s:
            print(i)
            break
