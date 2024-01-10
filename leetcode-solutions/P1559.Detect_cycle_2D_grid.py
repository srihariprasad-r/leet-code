# wrong submission

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        paths = {(i, j): (i, j) for i in range(len(grid))
                 for j in range(len(grid[0]))}
        rank = collections.Counter()

        def find(a):
            if a != paths[a]:
                return find(paths[a])

            return paths[a]

        def union(x, y):
            x1, y1 = find(x), find(y)

            if x1 == y1:
                return True

            if x1 != y1:
                if rank[x1] > rank[y1]:
                    paths[y1] = x1
                    rank[x1] += 1
                else:
                    paths[x1] = y1
                    # rank[y1] += 1

            return False

        a = False
        b = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i > 0 and grid[i-1][j] == grid[i][j]:
                    a = union((i-1, j), (i, j))
                if j > 0 and grid[i][j-1] == grid[i][j]:
                    b = union((i, j-1), (i, j))

                if a and b:
                    return True

        return False

# wrong submission
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        q = deque()
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        q.append((0,0, -1, -1))
        visited[0][0] = 1

        while q:
            i, j, src_i, src_j = q.popleft()
            # if visited[i][j]: return True

            direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]

            for d in direction:
                x = i + d[0]
                y = j + d[1]
                if x > -1 and x < len(grid) and y > -1 and y < len(grid[0])\
                    and not visited[x][y] and grid[x][y] == grid[i][j]:
                    if visited[i][j]: return True
                    visited[x][y] = 1
                    q.append(x, y, i, j)

        return False