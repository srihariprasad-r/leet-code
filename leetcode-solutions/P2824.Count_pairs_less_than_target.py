# wrong submission
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        cnt = 0
        def bs(idx, tgt, n):
            l = idx
            r = len(nums) - 1

            while l < r:
                mid = l + (r-l)//2

                if tgt - n <= nums[mid]:
                    r = mid
                else: 
                    l = mid + 1

            return l - idx

        for i in range(len(nums)):
            res = -1
            # if not (nums[i] >= target and nums[i] > 0):
            res = bs(i+1, target, nums[i])
            if 0 <= res <= len(nums) - 1:
                cnt += res

        return cnt