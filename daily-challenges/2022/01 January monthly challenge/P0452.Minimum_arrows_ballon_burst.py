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