class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        pos = [0] * len(nums)
        neg = [0] * len(nums)        
        
        if nums[0] > 0:
            pos[0] = 1
        elif nums[0] < 0:
            neg[0] = 1
        
        result = pos[0]
        
        for i in range(1, len(nums)):
            if nums[i] > 0:
                pos[i] = 1 + pos[i-1]
                neg[i] = 1 + neg[i-1] if neg[i-1] > 0 else 0
            elif nums[i] < 0:
                pos[i] = 1 + neg[i-1] if neg[i-1] > 0 else 0                
                neg[i] = 1 + pos[i-1] 
            
            result = max(result, pos[i])
        
        return result