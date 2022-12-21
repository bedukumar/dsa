dp = [-1]*100


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif dp[n] != -1:
        return dp[n]
    dp[n] = fib(n-1)+fib(n-2)
    return dp[n]


print(fib(8))
