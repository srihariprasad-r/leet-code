class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        tsum = 0
        dp_arr = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == len(matrix)-1 and matrix[i][j] != 0:
                    dp_arr[i][j] = 1
                elif j == len(matrix[0]) -1 and matrix[i][j] != 0:
                    dp_arr[i][j] = 1
                tsum += dp_arr[i][j]
           
        for i in range(len(matrix)-2, -1, -1):
            for j in range(len(matrix[0])-2, -1, -1):
                if matrix[i][j] == 0:
                    dp_arr[i][j] = 0
                else:
                    dp_arr[i][j] = min(dp_arr[i+1][j], dp_arr[i][j+1], dp_arr[i+1][j+1]) + 1
                    tsum += dp_arr[i][j]
    
        return tsum