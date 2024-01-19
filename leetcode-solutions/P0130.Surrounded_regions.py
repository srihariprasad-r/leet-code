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

        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O':
                    q.append((i, j))
                    visited[i][j] = 1

        while q:
            x, y = q.popleft()

            visited[x][y] = 1
            surrounded = False

            for d in directions:
                newx = x + d[0]
                newy =  y + d[1]
                if newx > 0 and newx < m -1 and newy > 0 and newy < n- 1 and \
                    board[newx][newy] == 'X' and not visited[newx][newy]:
                    surrounded = True
                    visited[newx][newy] = 1
                # else:
                #     surrounded = False

            if surrounded:
                board[x][y] = 'X'

        return board