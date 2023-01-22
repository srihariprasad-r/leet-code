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

# Method 2

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
            right = len(nums)
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

            return right

        lt = searchleft(nums)
        if lt == len(nums) or nums[lt] != target:
            return [-1, -1]
        return [lt, searchright(nums)-1]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bs_left(target):
            l = 0
            r = len(nums) - 1

            while l <= r:
                m = (l+r)//2

                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1

            return l

        def bs_right(target):
            l = 0
            r = len(nums)

            while l < r:
                m = l + (r-l) // 2

                if nums[m] > target:
                    r = m
                else:
                    l = m + 1

            return r

        idx = bs_left(target)
        idx1 = bs_right(target) - 1

        if idx >= 0 and idx < len(nums) and nums[idx] == target:
            return [idx, idx1]
        else:
            return [-1, -1]
