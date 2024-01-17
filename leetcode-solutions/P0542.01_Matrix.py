class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])

        for row in range(m):
            for col in range(n):
                if mat[row][col]:
                    mat[row][col] = float('inf')
                    if row > 0 and mat[row][col] > mat[row-1][col] + 1:
                        mat[row][col] = mat[row-1][col] + 1
                    if col > 0 and mat[row][col] > mat[row][col-1] + 1:
                        mat[row][col] = mat[row][col-1] + 1

        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                if mat[row][col]:
                    if row < m-1 and mat[row][col] > mat[row+1][col] + 1:
                        mat[row][col] = mat[row+1][col] + 1
                    if col < n - 1 and mat[row][col] > mat[row][col+1] + 1:
                        mat[row][col] = mat[row][col+1] + 1

        return mat

# Method 2
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        m = len(mat)
        n = len(mat[0])
        visited = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        directions = [(0, -1),(0,1), (-1,0), (1,0)]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    visited[i][j] = 1

        while q:
            x, y, dst = q.popleft()
            mat[x][y] = dst

            for d in directions:
                newx = x + d[0]
                newy = y + d[1]
                if newx > -1 and newx < m and newy > -1 and newy < n \
                and visited[newx][newy] == 0:
                    if mat[newx][newy] == 1:
                        q.append((newx, newy, dst + 1))
                        visited[newx][newy] = 1

        return mat