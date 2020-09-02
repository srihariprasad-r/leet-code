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
                if i + 1 < len(nums) and  max_prod < max_prod * nums[i+1]:
                    start = i + 1
                    tmp = 1                                
                    max_prod = 1
                    continue                    
                elif i + 1 == len(nums):
                    return end - start + 1
                                    
            tmp  = tmp * nums[i]                                                            
            
            if tmp > 0 and max_prod < tmp:    
                max_prod = tmp 
                end = i    
            elif tmp < 0 and max_prod < tmp:                
                start = i + 1
                tmp = 1
                max_prod = 1
            elif tmp > 0 and max_prod > tmp:
                end= i + 1
                tmp = 1
                max_prod = 1gi                                                        
            
        return end - start + 1