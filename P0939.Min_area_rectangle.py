class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        visited = set()
        mn = float('inf')

        for x1, y1 in points:
            for x2, y2 in visited:
                if (x1, y2) in visited and (x2, y1) in visited:
                    mn = min(mn, abs(x1-x2) * abs(y1-y2))
            visited.add((x1, y1))

        return mn if mn < float('inf') else 0
