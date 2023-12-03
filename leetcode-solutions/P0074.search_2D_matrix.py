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

# Method 2

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m * n - 1

        while l <= r:
            mid = l + (r-l)//2

            row = mid // n
            col = mid % n

            if matrix[row][col] < target:
                l = mid + 1
            elif matrix[row][col] > target:
                r = mid - 1
            else:
                return True

        return False

#Method 3
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs(arr, target):
            l = 0
            h = len(arr) - 1

            while l <= h:
                mid = l + (h-l)//2
                if arr[mid] == target:
                    return mid

                if arr[mid] >= target:
                    h = mid -  1
                else:
                    l = mid + 1
            
            return -1 

        for i in range(len(matrix)):
            idx = bs(matrix[i], target)
            if  idx == -1:
                continue
            else:
                return True

        return False