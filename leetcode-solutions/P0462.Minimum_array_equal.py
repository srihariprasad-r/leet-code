# wrong submission
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r-l)//2

            if sum(abs(c - nums[mid]) for c in nums) <= nums[mid]:
                r = mid 
            else:
                l = mid + 1

        return sum(abs(c - nums[l]) for c in nums)