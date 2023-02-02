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


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()

        res = [-1] * (len(nums) - k + 1)

        for i in range(len(nums)):
            while q and q[0] <= i - k:
                q.popleft()

            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            if i >= k - 1:
                res[i-k+1] = nums[q[0]]

        return res