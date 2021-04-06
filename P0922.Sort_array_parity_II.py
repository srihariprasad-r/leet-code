class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(nums)
        oddidx = 1 
        evenidx = 0
        for i in range(len(nums)):
            if nums[i]%2:
                ans[oddidx] = nums[i]
                oddidx += 2
            else:
                ans[evenidx] = nums[i]
                evenidx += 2     
        
        return ans