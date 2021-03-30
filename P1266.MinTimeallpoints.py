class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        maxsteps = 0
        for i in range(len(points)-1):
            start_x, start_y = points[i][0], points[i][1]
            end_x, end_y  = points[i+1][0], points[i+1][1]
            diff_x = abs(start_x- end_x)
            diff_y = abs(start_y - end_y)
            maxsteps += max(diff_x , diff_y)
            
        return maxsteps