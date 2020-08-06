class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for c in nums:
            if nums.count(c) == 1:
                return c            