class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r = len(matrix)
        c = len(matrix[0])

        if r == 0 or c == 0:
            return false

        def ok(mat, idx, target):
            r = len(mat)
            c = len(mat[0])
            return mat[idx/c][idx % c] >= target

        low = -1
        high = r * c - 1

        while low + 1 < high:
            mid = low + (high-low) // 2

            if ok(matrix, mid, target):
                high = mid
            else:
                low = mid

        return matrix[high/c][high % c] == target
