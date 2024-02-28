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

# Method 2
class Solution:
    def searchInsert(self, arr: List[int], target: int) -> int:
        l = 0
        r = len(arr)

        while l < r:
            mid = l + (r - l) // 2

            if arr[mid] == target:
                return mid

            if arr[mid] < target:
                l = mid + 1
            else:
                r = mid

        return l      