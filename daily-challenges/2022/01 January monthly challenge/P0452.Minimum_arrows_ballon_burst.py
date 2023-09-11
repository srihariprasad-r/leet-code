class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        newlst = sorted(points, key=lambda x:x[1])
        cnt = 0
        end = float('-inf')
        
        for baloon in newlst:
            if end < baloon[0]:
                end = baloon[1]
                cnt += 1
                
        return cnt
    
# Method 2 - almost same

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])
        cnt = 1
        x = points[0][1]

        for p in points:
            if p[0] > x:
                cnt += 1
                x = p[1]

        return cnt
