# wrong submission
class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        pq = deque()
        res = 0

        k = k1 + k2

        for a,b in zip(nums1, nums2):
            pq.append(abs(a-b))

        while k > 0:
            el = pq.pop()
            if el == 0: break
            pq.append(el-1)
            k -= 1
        
        while pq:
            el = pq.pop()
            res += el**2

        return res