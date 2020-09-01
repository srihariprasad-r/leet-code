class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_prod = 1
        tmp = 1
        
        start, end = 0, 0 
        
        while nums and nums[0] == 0:
            nums = nums[1:]

        if len(nums) == 0:
            return 0
        elif len(nums) == 1 and nums[0] > 0:
            return 1
        elif len(nums) == 1 and nums[0] < 0:
            return 0
                                
        for i in range(len(nums)):
            if nums[i] == 0:   
                tmp = 1
                continue               
                                    
            if max_prod < tmp * nums[i]:   
                tmp  = tmp * nums[i]                
                max_prod = tmp 
                end = i                                
            else:
                tmp = nums[i]
            
        return end - start + 1