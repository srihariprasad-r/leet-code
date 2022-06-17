class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """        
        newlist = [-x for x in stones]
        
        heapq.heapify(newlist)
        
        while len(newlist) > 1:
            heapq.heappush(newlist, heapq.heappop(newlist) - heapq.heappop(newlist))
            
        return -newlist[0]