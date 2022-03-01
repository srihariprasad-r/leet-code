# Wrong submission

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = 1
        i = j = 0

        while right < len(nums):
            if nums[right] > 0:
                j = right + 1
                while j < len(nums):
                    if nums[j] < 0:
                        break
                    j += 1
                if j < len(nums) and right < len(nums):
                    nums[j], nums[right] = nums[right], nums[j]
                    if j - right > 1:
                        nums[j], nums[j-1] = nums[j-1], nums[j]
                # left += 1
                right += 2
            elif nums[left] < 0:
                i = right
                while i < len(nums):
                    if nums[i] > 0:
                        break
                    i += 1
                if i < len(nums) and left < len(nums):
                    nums[i], nums[left] = nums[left], nums[i]
                    if i - left > 1:
                        nums[i], nums[i-1] = nums[i-1], nums[i]
                left += 2
                # right += 1
            else:
                left += 2
                right += 2

        return nums
