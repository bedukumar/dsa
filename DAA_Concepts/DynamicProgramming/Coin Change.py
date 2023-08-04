def coinChange(self, coins: List[int], amount: int) -> int:
  dp = [inf]*(amount+1)
  dp[0] = 0
  for i in range(amount+1):
    for j in coins:
      if i-j >=0 :
        dp[i] = min(1+dp[i-j],dp[i])
  if dp[amount] != inf:
    return dp[amount]
  else:
    return -1




"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

"""
