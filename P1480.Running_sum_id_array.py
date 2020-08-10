class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if i == 0:
                nums[0] = nums[i]
            else:
                nums[i] = nums[i-1] + nums[i]
        
        return nums            