class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        s = 0

        for i in range(len(nums)):
            mn_val = float('inf')
            mx_val = float('-inf')
            for j in range(i, len(nums)):
                mn_val = min(mn_val, nums[j])
                mx_val = max(mx_val, nums[j])
                diff = mx_val - mn_val
                s += diff

        return s

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0

        ple = []
        nle = []

        leftMin = [len(nums)] * len(nums)
        rightMin = [-1] * len(nums)

        for i in range(len(nums)):
            while ple and nums[ple[-1]] > nums[i]:
                leftMin[ple.pop()] = i
            ple.append(i)

        for i in range(len(nums)-1, -1, -1):
            while nle and nums[nle[-1]] >= nums[i]:
                rightMin[nle.pop()] = i
            nle.append(i)


        pge = []
        nge = []

        leftMax = [len(nums)] * len(nums)
        rightMax = [-1] * len(nums)

        for i in range(len(nums)):
            while pge and nums[pge[-1]] < nums[i]:
                leftMax[pge.pop()] = i
            pge.append(i)

        for i in range(len(nums)-1, -1, -1):
            while nge and nums[nge[-1]] <= nums[i]:
                rightMax[nge.pop()] = i
            nge.append(i)

        for i in range(len(nums)):
            l = leftMax[i]
            r = rightMax[i]
            res += nums[i]* (i-l) * (r-i) 

        for i in range(len(nums)):  
            l = leftMin[i]
            r = rightMin[i]                  
            res -= nums[i] * (i-l) * (r-i) 

        return res