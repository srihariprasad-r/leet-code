class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        rslt = []
        
        for i in range(len(nums)):
            s = nums[i]
            rslt.append(s)
            for j in range(i+1, len(nums)):
                s += nums[j]
                rslt.append(s)
                
        rslt.sort()
        
        return sum(rslt[left-1:right]) % 1000000007