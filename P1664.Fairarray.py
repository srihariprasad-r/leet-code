class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n  = 0
    
        left = [0, 0]
        right = [sum(nums[0::2]), sum(nums[1::2])]
    
        for i in range(len(nums)):
            right[i%2] -= nums[i]
            if left[0] + right[1] == right[0] + left[1] :
                n += 1
            left[i%2] += nums[i]
        
        return n