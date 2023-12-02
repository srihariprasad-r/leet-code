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

# Method 3 - wrong submission


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        if len(nums) == 1:
            return nums[0]
        if nums[l] < nums[r]:
            return nums[l]

        while l <= r:
            mid = l + (r-l)//2

            if mid > 0 and nums[mid-1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1

        return -1

# Method 4
class Solution:
    def findMin(self, arr: List[int]) -> int:
        ans = float('inf')
        l = 0
        h = len(arr) - 1

        if arr[l] <= arr[h]: return arr[l]

        while l <= h:
            mid = l + (h-l) // 2
            if arr[mid] >= arr[l]:
                ans = min(ans, arr[l])
                l = mid + 1
            else:
                h = mid - 1
                ans = min(ans, arr[mid])

        return ans