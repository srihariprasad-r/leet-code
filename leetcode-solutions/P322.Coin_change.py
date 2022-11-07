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
            
# Method 2 - wrong submission
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        def dfs(idx, c, t, dp, a=[]):
            if idx > n or t < 0:
                return float('inf')

            if t == 0:
                dp[idx] = c
                return c

            if dp[idx] > 0:
                return dp[idx]

            res = float('inf')
            take = float('inf')
            no_take = float('inf')

            for i in range(idx, n):
                if t >= coins[idx]:
                    take = dfs(idx, c+1, t-coins[idx], dp, a + [coins[idx]])
                no_take = dfs(idx+1, c, t, dp, a)

            res = min(take, no_take)

            dp[idx] = res

            return dp[idx]

        dp = [0] * (amount+1)

        o = dfs(0,  0, amount, dp)

        return -1 if o == float('inf') else o
