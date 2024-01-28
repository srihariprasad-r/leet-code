# wrong submission

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [(0, -1), (0, 1), (-1,0),(1,0)]
        mx = float('inf')
        visited = [[0 for _ in range(len(heights[0]))] for _ in range(len(heights))]
        distance = [[0 for _ in range(len(heights[0]))] for _ in range(len(heights))]

        l =[(heights[0][0], (0, 0))]
        heapq.heapify(l)
        visited[0][0] = 1        
        
        while l:
            dist, a = heapq.heappop(l)
   
            if a[0] == len(heights)-1 and a[1] == len(heights[0])-1:
                return dist

            for d in directions:
                newx = a[0] + d[0]
                newy = a[1] + d[1]
                if newx > -1 and newx < len(heights) \
                    and newy > -1 and newy < len(heights[0]) \
                    and visited[newx][newy] == 0:
                    newdist = max(abs(heights[a[0]][a[1]] - heights[newx][newy]), dist)
                    if newdist < distance[newx][newy]:
                        distance[newx][newy] = newdist
                        heapq.heappush(l, (newdist, (newx, newy)))
                        visited[newx][newy] = 1

        return 0