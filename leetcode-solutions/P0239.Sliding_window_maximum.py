class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []

        pq = []

        for i, el in enumerate(nums):
            while pq and i >= k and pq[0][1] <= i - k:
                heapq.heappop(pq)

            heapq.heappush(pq, (-el, i))

            if i >= k-1:
                ans.append(-pq[0][0])

        return ans
