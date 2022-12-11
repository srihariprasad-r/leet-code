class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        res = {}
        for i in range(len(grid)):
            heaplist = [-x for x in grid[i]]
            while heaplist:
                maxval = float('-inf')
                heapq.heapify(heaplist)
                el = heapq.heappop(heaplist)
                maxval = max(maxval, -el)
                if len(heaplist) not in res:
                    res[len(heaplist)] = maxval
                else:
                    res[len(heaplist)] = max(maxval, res[len(heaplist)])

        return sum(x for x in res.values())
