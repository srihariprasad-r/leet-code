class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted([x**2 for x in A])


# Method 2

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 1:
            return [nums[0]**2]

        small_index = float('inf')
        min_el = float('inf')
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] *= -1

            if min_el > nums[i]:
                min_el = nums[i]
                small_index = i

        left = small_index - 1
        right = small_index
        idx = 0
        arr = [0] * len(nums)

        while left >= 0 and right < len(nums):
            lt = nums[left]**2
            rt = nums[right] ** 2

            if lt > rt:
                arr[idx] = rt
                right += 1
            else:
                arr[idx] = lt
                left -= 1
            idx += 1

        while left >= 0:
            arr[idx] = nums[left]**2
            left -= 1
            idx += 1

        while right < len(nums):
            arr[idx] = nums[right]**2
            right += 1
            idx += 1

        return arr