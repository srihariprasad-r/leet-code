class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tgt = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= tgt:
                tgt = i

        return True if tgt == 0 else False
