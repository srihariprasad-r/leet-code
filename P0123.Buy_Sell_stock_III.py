class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        left = [0] * len(prices)
        right = [0] * len(prices)
        minleft = prices[0]

        for i in range(1, len(prices)):
            left[i] = max(left[i-1], prices[i] - minleft)
            minleft = min(minleft, prices[i])

        maxright = prices[-1]

        for i in range(len(prices)-2, -1, -1):
            right[i] = max(right[i+1], maxright - prices[i])
            maxright = max(maxright, prices[i])

        profit = right[0]
        for i in range(1, len(prices)):
            profit = max(profit, left[i-1]+right[i])

        return profit
