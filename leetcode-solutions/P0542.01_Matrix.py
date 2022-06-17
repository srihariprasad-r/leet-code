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
