# wrong submission
class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        j = len(nums) - 1
        i = j - 1
        ans = 0

        while i >= 0 and j >= 0:
            i = j - 1
            if nums[j] > nums[i]:
                j = i - 1
                i -= 1
                ans += 2
            else:
                j = i
                i -= 1
        
        return len(nums) - ans