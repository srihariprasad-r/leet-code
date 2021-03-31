class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_prod = 1
        sorted_array = sorted(nums, key=lambda x: -x)
        
        for i in range(2):
            max_prod *= sorted_array[i] - 1
            
        return max_prod