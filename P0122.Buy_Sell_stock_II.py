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
