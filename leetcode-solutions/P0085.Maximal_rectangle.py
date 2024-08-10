class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        ans = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0': continue
                for row in range(i, m):
                    for col in range(j, n):
                        if matrix[row][col] == '0': continue
                        ones = True
                        for p in range(i, row+1):
                            for q in range(j, col+1):
                                if matrix[p][q] == '0': 
                                    ones = False
                                    break
                                if not ones: break
                        if ones: ans = max(ans, (row-i+1)*(col-j+1))
                                        
        return ans