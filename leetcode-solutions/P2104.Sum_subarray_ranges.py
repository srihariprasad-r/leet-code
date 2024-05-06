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

# wrong submission
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0

        ple = []
        nle = []

        leftMin = [0] * len(nums)
        rightMin = [0] * len(nums)

        for i in range(len(nums)):
            while ple and nums[ple[-1]] > nums[i]:
                ple.pop()
            leftMin[i] = i - ple[-1] if ple else i + 1

        for i in range(len(nums)-1, -1, -1):
            while nle and nums[nle[-1]] > nums[i]:
                nle.pop()
            rightMin[i] = nle[-1] - i if nle else len(nums) - i

        pge = []
        nge = []

        leftMax = [0] * len(nums)
        rightMax = [0] * len(nums)

        for i in range(len(nums)):
            while pge and nums[pge[-1]] < nums[i]:
                pge.pop()
            leftMax[i] = i - pge[-1] if pge else i + 1

        for i in range(len(nums)-1, -1, -1):
            while nge and nums[nge[-1]] < nums[i]:
                nge.pop()
            rightMax[i] = nge[-1] - i if nge else len(nums) - i


        for i in range(len(nums)):
            res += nums[i]* (max(leftMax[i] , rightMax[i]) - min(rightMin[i] , leftMin[i]))

        return res