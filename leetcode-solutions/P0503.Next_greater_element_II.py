class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = nums + nums

        res = [-1]* n

        i = 0
        while i < n:
            j = i + 1
            while j < n*2:
                if nums[i] < nums[j]:
                    res[i] = nums[j]
                    break
                else:
                    j += 1
            i += 1

        return res