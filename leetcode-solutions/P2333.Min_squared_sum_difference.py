# wrong submission
class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        pq = []
        res = 0

        heapq.heapify(pq)

        k = k1 + k2

        for a,b in zip(nums1, nums2):
            heapq.heappush(pq, -abs(a-b))

        while pq and k > 0:
            el = heapq.heappop(pq)
            if el != 0: 
                heapq.heappush(pq, abs(el)-1)
                k -= 1

        while pq:
            el = heapq.heappop(pq)
            res += el*el

        return res