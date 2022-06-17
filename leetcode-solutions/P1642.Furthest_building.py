class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        lst = []
        for i in range(len(heights) - 1):
            j = i + 1
            diff = heights[j] - heights[i]
            if diff > 0:
                heapq.heappush(lst, diff)
            if len(lst) > ladders:
                bricks -= heapq.heappop(lst)
            
            if bricks < 0:
                return i
        
        return len(heights) - 1
