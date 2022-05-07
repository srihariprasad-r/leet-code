#TLE submission

class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        cnt = 0
        for i in range(len(nums)):
            csum = nums[i]
            j = i+1
            if csum == goal:
                cnt += 1
            while j < len(nums):
                csum += nums[j]
                if csum == goal:
                    cnt += 1
                if csum > goal:
                    break
                j += 1

        return cnt
