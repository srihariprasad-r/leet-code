class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverse(left, right):
            while left < right:
                tmp = nums[right]
                nums[right] = nums[left]
                nums[left] = tmp
                left += 1
                right -= 1

        n = len(nums)
        k = k % len(nums)
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n - 1)