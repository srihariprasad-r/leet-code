class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        a = 0
        b = len(nums) - 1

        while(a <=b):
            mid = (a + b) /2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                a = mid + 1    
            elif nums[mid] > target:
                b = mid - 1            
    
        return a