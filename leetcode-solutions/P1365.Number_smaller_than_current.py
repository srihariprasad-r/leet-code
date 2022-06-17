class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
                
        new_sorted_list = sorted(nums)
        output = [0] * len(nums)
        
        
        for i in range(len(nums)):
            output[i] = new_sorted_list.index(nums[i])

        return output                          