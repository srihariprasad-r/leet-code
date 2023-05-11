# wrong submission

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        visited = [[0 for _ in range(len(board[0]))]  for _ in range(len(board))]
        res = set()

        def dfs(i, j, w, s):
            if len(w) < len(s) : return 
            if len(w) == len(s):
                if s == w: res.add(w)
                return

            if 0 <= i < len(board) and 0 <= j < len(board[0]):
                if visited[i][j] != 1 :
                    visited[i][j] = 1
                    s += board[i][j]
                    dfs(i + 1, j, w, s)
                    dfs(i, j + 1, w, s)
                    dfs(i, j -1 , w, s)
                    dfs(i-1, j, w, s)
                    # s -= board[i][j]
                    visited[i][j] = 0

            return res

        for w in words:
            dfs(0, 0, w, '')

        return res