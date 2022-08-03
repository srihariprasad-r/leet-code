class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)

        presum = [0]

        for i in range(n):
            presum.append(presum[-1]+nums[i])

        q = collections.deque()

        ans = sys.maxsize

        for idx, el in enumerate(presum):
            while q and el - presum[q[0]] >= k:
                ans = min(ans, idx - q.popleft())

            while q and el <= presum[q[-1]]:
                q.pop()

            q.append(idx)

        return ans if ans < sys.maxsize else -1
