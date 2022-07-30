# Wrong submission

class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        if len(nums) == 1:
            return 1
        
        if len(nums) == 2:
            return 2
        
        max_idx = nums.index(max(nums)) 
        min_idx = nums.index(min(nums))

        return min(max_idx + 1 , n - min_idx , min_idx + 1 + n - max_idx)