# TLE submission

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        
        for i in range(len(height) - 1):
            for j in range(i+1, len(height)):
                res = max(res, min(height[j], height[i]) * (j-i))
                
                
        return res