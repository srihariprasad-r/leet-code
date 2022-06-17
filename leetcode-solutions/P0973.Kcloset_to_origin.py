class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        sqrt = []
        res = []
        for i in range(len(points)):
            sqrt_val = points[i][0] *  points[i][0] +  points[i][1] *  points[i][1]
            sqrt.append((sqrt_val, points[i]))
        
        heapq.heapify(sqrt)
        for i in range(k):
            res.append(heapq.heappop(sqrt)[1])
        
        return res