class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end)/2
            
            if nums[mid] == target:
                return mid
            
            if nums[start] <= nums[mid]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
                    
        return -1

# Method 2
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end)/2

            if nums[mid] == target:
                return mid

            if nums[mid] > nums[end]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1

# Method 3 - similar to above


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r-l+1) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] > nums[l]:
                if nums[l] <= target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[r] >= target and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1

# almost same
class Solution:
    def search(self, arr: List[int], target: int) -> int:
        l = 0
        h = len(arr) - 1

        while l <= h:
            mid = l + (h-l) // 2
            if target == arr[mid]: return mid

            if arr[mid] >= arr[l]:
                if target <= arr[mid] and target >= arr[l]:
                    h = mid - 1
                else:
                    l = mid + 1
            else:
                if target >= arr[mid] and target <= arr[h]:
                    l = mid + 1
                else:
                    h = mid - 1

        return -1
    
# almost same except '=' condition
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r-l)//2

            if target == nums[mid]: return mid

            if nums[l] <= nums[mid]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target <= nums[r] and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1 if nums[l] != target else l