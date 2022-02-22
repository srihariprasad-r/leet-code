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


# Method 2

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 1

        while right < len(nums):
            if nums[left] != 0:
                left += 1
                right += 1
            elif nums[right] == 0:
                right += 1
            else:
                tmp = nums[right]
                nums[right] = nums[left]
                nums[left] = tmp

        return nums