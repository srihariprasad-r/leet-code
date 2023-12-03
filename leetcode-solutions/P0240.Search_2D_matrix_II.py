class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        
        res = False
        
        for i in range(len(matrix)):
            if self.binarysearch(matrix[i], target):
                return True
            else:
                res = self.binarysearch(matrix[i],target)
        
        return res
    
    def binarysearch(self, row, target):
        low, high = 0, len(row)-1
        
        while low <= high:
            mid = low + (high-low)//2
            
            if row[mid] == target:
                return True
            elif row[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
    
# method 2
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