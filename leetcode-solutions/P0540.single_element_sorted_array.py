class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if ((mid % 2 == 0 and mid + 1 < len(nums) and nums[mid] == nums[mid+1])
                    or (mid % 2 == 1 and nums[mid] == nums[mid-1])):
                left = mid + 1
            else:
                right = mid

        return nums[left]

# Method 2
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while l < r:
            mid = l + (r-l) //2
 
            if nums[mid] == nums[mid-1]:
                if mid % 2:
                    l = mid +1
                else:
                    r = mid - 1
            elif nums[mid] == nums[mid+1]:
                if mid % 2:
                    r = mid -1 
                else:
                    l = mid + 1
            else:
                return nums[mid]

        return nums[l]