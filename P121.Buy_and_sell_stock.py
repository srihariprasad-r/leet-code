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