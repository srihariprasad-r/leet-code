class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        discount = [-1] * len(prices)
        for i in range(len(prices)):
            j = i+ 1
            while j < len(prices):
                if prices[j] <= prices[i]:
                    discount[i] = prices[i] - prices[j]
                    break
                j += 1
            
            if discount[i] == -1:
                discount[i] = prices[i]
        
        return discount