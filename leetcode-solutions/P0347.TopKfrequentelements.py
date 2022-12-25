class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        dict = Counter(nums)
        heaplist = [(-val, key) for key, val in dict.items()]
        heapq.heapify(heaplist)
        for i in range(k):
            res.append(heapq.heappop(heaplist)[1])
        
        return res

# Method 2 - slightly different


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = Counter(nums)
        arr = []
        res = []
        for m, v in mp.items():
            arr.append((-v, m))

        heapq.heapify(arr)
        j = 0
        while j < k:
            el = heapq.heappop(arr)
            res.append(el[1])
            j += 1

        return res
