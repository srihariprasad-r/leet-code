class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid

        return left

# Method 2
class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1: return 0
        # first element is peak
        if arr[0] > arr[1] : return 0
        # last element is peak
        if arr[n-1] > arr[n-2]: return n-1
        # rest all elements
        l = 1
        h = len(arr) - 2

        while l <= h:
            mid = l + (h-l) // 2
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            
            if arr[mid] > arr[mid-1]:
                l = mid + 1
            else:
                h = mid - 1
        
        return 

# Method 3
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1 : return 0
        if len(nums) == 2: return 0 if nums[0] > nums[1] else 1

        l = 0
        r = len(nums)-1

        while l < r:
            mid = l + (r-l)//2

            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid

            if nums[mid] > nums[mid-1] and nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid

        return l if nums[l] > nums[r] else r