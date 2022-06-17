class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_dict = {i: nums.count(i) for i in nums}
        
        unique_sum = 0
        
        for k, v in unique_dict.items():
            if v == 1:
                unique_sum += k
                
        return unique_sum