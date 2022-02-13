# wrong submission, needs rework

class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt, i = 0, 0
        stck = []
        stck.append(nums[i])
        
        while i <= len(nums) - 2 - 1:
            j , k = i + 2, i + 1
            if not(stck[-1] != nums[k] and stck[-1] == nums[j]):
                if stck[-1] != nums[j]: nums[j] = stck[-1]
                cnt += 1
            if stck:
                stck.pop()
                stck.append(nums[k])
            i += 1
            
        return cnt