class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if nums.count(0) > 0:
            return nums.sort(key=lambda x: 1 if x == 0 else 0)
        else:
            return nums                