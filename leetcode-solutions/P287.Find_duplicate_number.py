class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return [x for x in nums if nums.count(x) > 1][0]