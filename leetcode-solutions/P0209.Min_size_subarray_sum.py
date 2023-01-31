class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort()
        st, rsum = 0, 0

        mlen = float('inf')

        for i in range(len(nums)):
            rsum += nums[i]
            while rsum >= target:
                mlen = min(mlen, i - st+1)
                rsum -= nums[st]
                st += 1

        return 0 if mlen == float('inf') else mlen

# Method 2 - almost similar to above

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        st = 0
        end = 0
        s = 0
        res = float('inf')

        while end < len(nums):
            s += nums[end]
            while s >= target:
                s -= nums[st]
                res = min(res, end - st + 1)
                st += 1
            end += 1

    
        return res if res != float('inf') else 0
