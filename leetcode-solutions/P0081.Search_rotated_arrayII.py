#Wrong submission

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0: return False
        
        if len(nums) == 1 and nums[-1] == target: return True
        
        left = 0
        right = len(nums) - 1
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True

            if nums[mid] < target:
                while mid +1 < len(nums):
                    if nums[mid] != nums[mid+1]:
                        break
                    mid += 1
            else:
                while mid - 1 > 0:
                    if nums[mid] != nums[mid-1]:
                        break
                    mid -= 1

            if mid + 1 < len(nums) and nums[mid] < nums[mid+1]:
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] > target:
                    right = mid -1
                else:
                    left = mid
        
        if nums[left] == target or nums[right] == target: return True
        
        return False