# Run time error

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
                
        if len(nums) == 1 and nums[-1] != 1:
            return 1
        
        res = filter(lambda x: x <= 0, nums)
        if len(res) == len(nums):
            return 1
        
        def binarySearch(nums, target):
            left = 0
            right = len(nums) - 1
        
            while left < right:
                mid = left + (right-left)//2
                if nums[mid] == target:
                    return True
                
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1
                    
            return True if nums[left] == target else False

        
        for m in range(1, long(sys.maxsize)):
            for i in range(len(nums)):
                if nums[i] > 0:
                    if binarySearch(nums, m):
                        continue
                    else:
                        return m