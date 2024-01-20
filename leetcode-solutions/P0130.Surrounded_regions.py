# wrong submission

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        q = deque()
        m = len(board)
        n = len(board[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        directions = [(-1, 0), (1,0),(0,1), (0,-1)]

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    if board[i][j] == 'O':
                        q.append((i, j))
                        visited[i][j] = 1

        while q:
            x, y = q.popleft()

            visited[x][y] = 1

            for d in directions:
                newx = x + d[0]
                newy =  y + d[1]
                if newx > 0 and newx < m -1 and newy > 0 and newy < n- 1 \
                    and not visited[newx][newy]:
                    if board[newx][newy] == 'O': 
                        board[newx][newy] = '#'
                    visited[newx][newy] = 1


        for i in range(1, m-1):
            for j in range(1,n-1):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                    
        return board