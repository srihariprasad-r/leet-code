class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = profit = buy = sell = 0
        n = len(prices) - 1

        while i < n:
            # get deepest valley to buy
            while i < n and prices[i+1] <= prices[i]:
                i += 1

            buy = prices[i]

            # get tallest mountain to sell
            while i < n and prices[i+1] > prices[i]:
                i += 1

            sell = prices[i]

            profit += sell - buy

        return profit

# Method 2


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0] * 2 for _ in range(len(prices))]
        # dp[i][0] - no share; dp[i][1] - with share
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            # yesterday no share, or with share - sell today
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            # yesterday had share or no share - buy today
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])

        return dp[-1][0]

# Method 3

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit 