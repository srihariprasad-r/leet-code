class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ln = len(nums)
        tot_sum = 0
        
        for i in range(ln+1) :
            tot_sum += i
        
        missing_num = tot_sum - sum(nums)
        
        return missing_num