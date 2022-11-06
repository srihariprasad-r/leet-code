class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1 for i in range(amount+1)]
        
        dp[0] = 0
        
        for i in range(1, len(dp)):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i-coins[j]] + 1)
                    
        if amount < dp[-1]:
            return -1
        else:
            return dp[amount]
            
# Method 2 - TLE
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        def dfs(idx, c, t):
            if idx > n or t > amount:
                return float('inf')

            if t == amount:
                return c

            res = float('inf')

            for i in range(idx, n):
                res = min(res, min(dfs(i, c+1, t+coins[i]), dfs(i+1, c, t)))

            return res

        o = dfs(0, 0, 0)

        return -1 if o == float('inf') else o
