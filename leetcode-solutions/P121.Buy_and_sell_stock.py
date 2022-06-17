class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min = 999999
        max = 0
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            elif (prices[i] - min > max):
                max = prices[i] - min
        
        return max

# Method 2


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        selling_price = 0
        max_profit = 0

        for i in range(len(prices)-1, -1, -1):
            selling_price = max(selling_price, prices[i])
            max_profit = max(max_profit, selling_price - prices[i])

        return max_profit
