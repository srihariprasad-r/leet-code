# wrong submission

class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        s = [0] * (len(nums) + 1)
        stck = [nums[0]]

        def f(l):
            s = 0
            for i in range(len(l)):
                s += l[i]

            return s >= (threshold/len(l))

        for i in range(1,len(nums)+1):
            s[i] = s[i-1] + nums[i-1]

        for i in range(1,len(nums)):
            if not f(stck):
                while stck:
                    stck.pop()
            stck.append(nums[i])

        return len(stck) if stck else -1