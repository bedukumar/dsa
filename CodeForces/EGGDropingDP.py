import sys


def eggDrop(n, k):
    dp = [[0 for j in range(k+1)] for i in range(n+1)]
    # print(dp)
    for e in range(1, n+1):
        for f in range(1, k+1):
            if e == 1:
                dp[e][f] = f
            elif f == 1:
                dp[e][f] = 1
            else:
                pj = 0
                mi = sys.maxsize
                mj = f-1
                while mj >= 0:
                    v1 = dp[e][mj]
                    v2 = dp[e-1][pj]
                    val = max(v1, v2)
                    mi = min(val, mi)
                    pj += 1
                    mj -= 1
                dp[e][f] = mi+1
    # print(dp)
    return dp[n][k]


n, k = map(int, input().split())
print(eggDrop(n, k))
