# Wrong submission

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        elif len(nums) == 1 and nums[0] == target:
            return [0, 0]

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                if mid - 1 >= 0 and nums[mid-1] == target:
                    return [mid-1, mid]
                elif mid + 1 < len(nums) and nums[mid+1] == target:
                    return [mid, mid+1]
                else:
                    return [mid, mid]

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return [right, right] if nums[right] == target else [-1, -1]