class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        for i in range(0,len(nums), 2):
            freq = nums[i:i+2][0]
            val = nums[i:i+2][1]
            result = [val]*freq
            output.append(result)
        
        return [i for item in output for i in item ]