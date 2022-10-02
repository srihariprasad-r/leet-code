# TLE submission

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        
        for i in range(len(nums)):
            j = i + 1

            while j < len(nums):
                if nums[i] > nums[j] * 2:
                    cnt += 1
                j += 1
            
        return cnt
            
            