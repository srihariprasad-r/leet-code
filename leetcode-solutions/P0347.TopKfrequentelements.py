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