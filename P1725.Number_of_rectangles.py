class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        res = []
        largest = - float('inf')
        for i in range(len(rectangles)):
            length, width = rectangles[i][0], rectangles[i][1]
            minarea = min(length, width)
            if minarea > largest: largest = minarea
            res.append(minarea)
        
        return len([x for x in res if x == largest])