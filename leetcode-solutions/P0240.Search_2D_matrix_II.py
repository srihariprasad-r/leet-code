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