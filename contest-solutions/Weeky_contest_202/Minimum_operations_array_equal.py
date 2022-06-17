class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        minNum = 1
        maxNum = (2 * (n-1)) + 1
        
        avgNum = (minNum + maxNum) / 2
        
        count = 0
        
        for i in range(0,n//2):
            if avgNum - ((2 * i) + 1) > 0:
                count += avgNum - ((2 * i) + 1)
        
        return count