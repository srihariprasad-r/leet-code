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
            