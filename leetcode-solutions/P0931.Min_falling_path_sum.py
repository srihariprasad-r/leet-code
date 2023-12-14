# TLE

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        mn = float('inf')
        dp = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        def recurse(i, j):
            if j < 0 or j >= len(matrix[0]) or i >= len(matrix):
                return float('inf')

            if i == len(matrix) - 1: return matrix[i][j]

            if dp[i][j] != -1: return dp[i][j]

            below = matrix[i][j] + recurse(i+1,j)
            left = matrix[i][j] + recurse(i+1,j - 1)
            right = matrix[i][j] + recurse(i+1,j + 1)

            dp[i][j] = min(below, min(left, right))

            return dp[i][j]

        for i in range(len(matrix[0])):
            mn = min(mn, recurse(0,i))

        return mn