class Solution(object):
    def waysToPartition(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        presum = [0]
        ans = 0

        for x in nums:
            presum.append(presum[-1]+x)

        presum.pop(0)

        rightcnt = Counter()
        leftcnt = Counter()

        for i in range(1, len(nums)):
            diff = presum[i-1] - (presum[-1] - presum[i-1])
            rightcnt[diff] += 1

        ans = rightcnt[0]

        for i in range(len(nums)):
            d = k - nums[i]

            ans = max(ans, leftcnt[d] + rightcnt[-d])

            diff = presum[i] - (presum[-1] - presum[i])
            rightcnt[diff] -= 1
            leftcnt[diff] += 1

        return ans
