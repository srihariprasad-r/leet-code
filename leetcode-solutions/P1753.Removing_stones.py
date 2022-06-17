class Solution(object):
    def maximumScore(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        heaplist = [-a, -b, -c]
        heapq.heapify(heaplist)
        res = 0

        while len(heaplist) > 1:
            res += 1
            val1 = -heapq.heappop(heaplist)-1
            val2 = -heapq.heappop(heaplist)-1 
            if val1 > 0:
                heapq.heappush(heaplist,-val1)
            if val2 > 0:
                heapq.heappush(heaplist,-val2)
            
        return res