class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        if nums[left] < nums[right]: return nums[left]
        
        while left + 1 < right:
            mid = left + (right-left)/2
            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid
            
        return min(nums[left], nums[right])

# Method 2

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        
        left = 0
        right = len(nums)- 1
        
        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
                
            mid = left + (right - left) // 2
            res = min(res, nums[mid])
            
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
                
        return res