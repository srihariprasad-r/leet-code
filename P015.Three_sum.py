class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()        
        res = []        
        for i in range(len(nums) - 2):
            
            if i > 0 and nums[i] == nums[i-1]: continue
                
            left = i+1
            right = len(nums) - 1        
            
            while left < right:
                csum = nums[i] + nums[left] + nums[right]      
                
                if csum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left +1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1                        
                    left += 1
                    right - 1
                    
                elif csum < 0:
                    left += 1
                    
                else:
                    right -= 1
        
        return res                     

# Method 2
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        
        nums.sort()
        
        res = []
        
        for i in range(len(nums)-2):
            low = i + 1
            high = len(nums) - 1
            while low != high:
                sum_el = nums[i] + nums[low] + nums[high]
                
                if sum_el == 0:
                    ot = [nums[i] , nums[low] , nums[high]]
                    if ot not in res:
                        res.append(ot)
                    low += 1
                elif sum_el < 0:
                    low += 1
                else:
                    high -= 1
                
                    
        return res