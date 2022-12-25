class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [1] * (len(nums) + 1)
        suffix = [1] * (len(nums) + 1)
        ans = []

        for i in range(len(nums)):
            prefix[i+1] = prefix[i] * nums[i]

        for i in range(len(nums)-1, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]

        for i in range(len(nums)):
            ans.append(prefix[i] * suffix[i+1])

        return ans

# Method 2 - slight variation

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(len(nums)-1, 0, -1):
            suffix[i-1] = suffix[i] * nums[i]

        for i in range(len(nums)):
            ans.append(prefix[i] * suffix[i])

        return ans
