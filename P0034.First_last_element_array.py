class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]

        def searchleft(nums):
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = left + (right-left)//2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            return left

        def searchright(nums):
            left = 0
            right = len(nums)
            while left < right:
                mid = left + (right-left)//2
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1

            return left

        lt = searchleft(nums)
        if lt == len(nums) or nums[lt] != target:
            return [-1, -1]
        return [lt, searchright(nums)-1]
