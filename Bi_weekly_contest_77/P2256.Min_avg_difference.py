class Solution(object):
    def minimumAverageDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_avg, min_idx = float('inf'), 0
        first_i = 0
        last_i = 0
        n = len(nums)

        prefix_sum = [0] * n
        avg = [0] * n
        total_sum = sum(nums)

        for i in range(len(nums)):
            prefix_sum[i] = sum(nums[0:i+1])

        for i in range(len(avg)):
            avg[i] = abs(prefix_sum[i]/(i+1) - ((total_sum -
                         prefix_sum[i])/(n-i-1) if (n-i-1) > 0 else 0))
            if avg[i] < min_avg:
                min_avg = avg[i]
                min_idx = i

        return min_idx
