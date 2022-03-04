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