class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        res = 0
        stck = []

        for i, num in enumerate(nums):
            step = 1
            while stck and nums[stck[-1]] <= nums[i]:
                step = max(step, dp[stck.pop()]+1)
            if stck:
                dp[i] = step
            res = max(res, dp[i])
            stck.append(i)
        
        return res
    
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stck = []
        el = [0] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            while stck and nums[stck[-1]] < nums[i]:
                el[i] = max(el[i]+1, el[stck.pop()])                               
            stck.append(i)

        return max(el)   