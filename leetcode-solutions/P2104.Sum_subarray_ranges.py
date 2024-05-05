# TLE
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        s = 0

        def getminvalue(arr):
            stck = []
            stck.append(arr[0])
            for i in range(1, len(arr)):
                while stck and stck[-1] > arr[i]: 
                    stck.pop()
                    stck.append(arr[i])

            return stck[-1]

        def getmaxvalue(arr):
            stck = []
            stck.append(arr[0])
            for i in range(1, len(arr)):
                while stck and stck[-1] < arr[i]:
                    stck.pop()
                    stck.append(arr[i])

            return stck[-1]

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                mn_val = getminvalue(nums[i:j+1])
                mx_val = getmaxvalue(nums[i:j+1])
                diff = mx_val - mn_val
                s += diff

        return s