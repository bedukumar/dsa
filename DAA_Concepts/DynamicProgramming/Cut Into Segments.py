def X(n, x, y, z,dp):
    if n == 0:
        return 0
    if n <0:
        return float('-inf')
    if dp[n]!=-1:
        return dp[n]
    a=X(n-x,x,y,z,dp)+1
    b=X(n-y,x,y,z,dp)+1
    c=X(n-z,x,y,z,dp)+1
    dp[n] = max(a,b,c)
    return dp[n]

def cutSegments(n, x, y, z):
    # Write your code here.
    dp=[-1]*(n+1)
    ans = X(n,x,y,z,dp)
    if ans < 0:
        return 0
    return ans

