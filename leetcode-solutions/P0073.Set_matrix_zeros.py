class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row_matrix = [-1 for _ in range(len(matrix))]
        col_matrix = [-1 for _ in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_matrix[i] = 0
                    col_matrix[j] = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row_matrix[i] == 0 or col_matrix[j] == 0:
                    matrix[i][j] = 0

        return matrix
