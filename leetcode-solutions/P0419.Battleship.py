class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def dfs(r,c):
            if r >= len(board) or r < 0 or c < 0 or c >= len(board[0]) or board[r][c] != 'X':
                return False

            board[r][c] = '.'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

            return True


        cnt = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    if dfs(i, j):  cnt += 1

        return cnt