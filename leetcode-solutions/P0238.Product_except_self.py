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
