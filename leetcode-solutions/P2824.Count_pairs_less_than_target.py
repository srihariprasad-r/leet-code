class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        cnt = 0
        def bs(idx, tgt, n):
            st = idx + 1
            l = idx + 1
            r = len(nums)

            while l < r:
                mid = l + (r-l)//2

                if tgt - n <= nums[mid]:
                    r = mid
                else: 
                    l = mid + 1

            return l - st

        for i in range(len(nums)):
            res = -1
            if nums[i] >= target and nums[i] > 0: 
                continue
            res = bs(i, target, nums[i])
            cnt += res

        return cnt