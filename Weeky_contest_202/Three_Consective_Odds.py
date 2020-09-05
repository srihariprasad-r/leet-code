class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        maxOdd = 0       
        for i, k in enumerate(arr):
            if k % 2 == 0:
                maxOdd = 0                
            elif k % 2 != 0 and i != 0:
                maxOdd += 1                
            elif i == 0 and k % 2 != 0:
                maxOdd += 1
        
            if maxOdd >= 3:
                return True 