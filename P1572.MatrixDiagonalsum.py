class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        sum_right, sum_left = 0, 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i == j:
                    sum_right += mat[i][j]
                    
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if len(mat)-1-i == j:
                    sum_left += mat[i][j]
                    
        return sum_left + sum_right if len(mat) %2 == 0 else sum_left + sum_right - mat[len(mat)//2][len(mat)//2]