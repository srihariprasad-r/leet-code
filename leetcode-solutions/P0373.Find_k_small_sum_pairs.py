class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(nums1)
        n = len(nums2)

        cnt = set()

        pq = []
        res = []

        for i in range(min(m, n)):
            heapq.heappush(pq, (nums1[0]+nums2[i], [nums1[0], nums2[i]], 0, i))
            cnt.add((0, i))

        while len(res) < k and pq:
            tsum, lst, i, j = heapq.heappop(pq)
            res.append(lst)

            if i < m - 1:
                if (i+1, j) not in cnt:
                    heapq.heappush(
                        pq, (nums1[i+1]+nums2[j], [nums1[i+1], nums2[j]], i+1, j))
                    cnt.add((i+1, j))

            if j < n - 1:
                if (i, j+1) not in cnt:
                    heapq.heappush(
                        pq, (nums1[i]+nums2[j+1], [nums1[i], nums2[j+1]], i, j+1))
                    cnt.add((i, j+1))

            # k -= 1

        return res
