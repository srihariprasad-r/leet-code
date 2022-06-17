class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumel = nums[0]
        res = 0
        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                res = max(res, sumel)
                sumel = 0
            sumel += nums[i]
            
        return max(res, sumel)