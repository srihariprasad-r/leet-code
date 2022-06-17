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
