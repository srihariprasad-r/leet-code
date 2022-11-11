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
        if amount == 0:
            return 0

        if len(coins) == 1 and ((amount % coins[-1] == 1)
                                or (coins[-1] % amount == 1)):
            return -1

        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins))]

        for i in range(len(coins)):
            include = float('inf')
            exclude = float('inf')
            for j in range(1, amount+1):
                if j >= coins[i]:
                    include = 1 + dp[i][j-coins[i]]
                if i > 0:
                    exclude = dp[i-1][j]
                dp[i][j] = min(include, exclude)

        return dp[-1][-1]