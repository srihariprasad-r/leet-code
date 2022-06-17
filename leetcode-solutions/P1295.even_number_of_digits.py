class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even = 0
        
        for i in range(len(nums)):
            cnt = 0
            idx = nums[i]
            while idx > 0:
                cnt += 1
                idx = idx // 10 
            
            if cnt % 2 == 0:
                even += 1
        
        return even