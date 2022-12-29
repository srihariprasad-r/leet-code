class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascals = []
        firstrow = []
        prevrow = []
        
        if numRows == 0: return pascals
        
        firstrow.append(1)
        pascals.append(firstrow)
                
        for i in range(1,numRows):
            currentrow = []
            prevrow = pascals[i-1]            
            currentrow.append(1)
            for j in range(1,i):
                currentrow.append(prevrow[j-1]+ prevrow[j])
            
            currentrow.append(1)            
            pascals.append(currentrow)        
        
        return pascals


# Method 2

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[1]*(i+1) for i in range(numRows)]

        for i in range(2, numRows):
            for j in range(1, i):
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

        return arr
