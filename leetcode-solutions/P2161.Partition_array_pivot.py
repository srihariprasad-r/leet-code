# Wrong submission

class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        mid = 0

        for i in range(len(nums)):
            if nums[i] == pivot:
                mid = i
                break

        left = 0
        right = mid - 1

        while left < right:
            if ((nums[left] >= nums[mid] and nums[right] <= nums[mid]) or
                    (nums[left] <= nums[mid] and nums[right] >= nums[mid])):
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            else:
                left += 1

        lastLeft = left
        left = mid + 1
        right = len(nums) - 1

        while left < right:
            if ((nums[left] <= nums[mid] and nums[right] >= nums[mid]) or
                    (nums[left] >= nums[mid] and nums[right] <= nums[mid])):
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            else:
                left += 1

        lastRight = right

        while lastLeft < mid and lastRight < len(nums):
            if nums[lastLeft] > nums[lastRight]:
                nums[lastLeft], nums[lastRight] = nums[lastRight], nums[lastLeft]
            lastLeft += 1
            lastRight += 1

        return nums