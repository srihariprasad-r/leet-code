class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        l = 0
        r = 50*50

        def dfs(x, y, mid):
            if visited[x][y]:
                return False
            if grid[x][y] <= mid:
                visited[x][y] = 1
                if x - 1 >= 0:
                    dfs(x-1, y, mid)
                if y - 1 >= 0:
                    dfs(x, y-1, mid)
                if x + 1 < len(grid):
                    dfs(x+1, y, mid)
                if y + 1 < len(grid[0]):
                    dfs(x, y+1, mid)
            return True

        while l < r:
            mid = (l + r) // 2
            visited = [[0 for i in range(len(grid))]
                       for _ in range(len(grid[0]))]
            dfs(0, 0, mid)
            if visited[-1][-1]:
                r = mid
            else:
                l = mid + 1

        return l