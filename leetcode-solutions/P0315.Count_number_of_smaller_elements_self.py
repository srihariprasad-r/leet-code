# wrong submission

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(nums)
        stck = []
        
        for i in range(len(nums)-1, -1, -1):
            cnt = 0
            while stck and nums[i] <= stck[-1]:
                stck.pop()
                
            if stck:
                ans[i] = len(stck)
            else:
                ans[i] = 0
                
            stck.append(nums[i])
        
        return ans