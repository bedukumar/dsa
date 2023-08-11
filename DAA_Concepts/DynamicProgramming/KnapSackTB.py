def knapSack(self,Weight, wt, val, n):
    t = [[0] * (Weight + 1) for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(Weight + 1):
            if i == 0 or j == 0:
                t[i][j] = 0
    
    for i in range(1, n + 1):  # Changed the variable name to 'i' from 'n'
        for j in range(1, Weight + 1):  # Changed the variable name to 'j' from 'W'
            if wt[i - 1] <= j:
                t[i][j] = max(val[i - 1] + t[i - 1][j - wt[i - 1]], t[i - 1][j])
            else:
                t[i][j] = t[i - 1][j]
    return t[n][Weight]
