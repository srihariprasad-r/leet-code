class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        pascals = []
        firstrow = []
        prevrow = []
        
        firstrow.append(1)
        pascals.append(firstrow)
        
        if rowIndex == 0: return pascals[rowIndex]        
                
        for i in range(1,rowIndex+1):
            currentrow = []
            prevrow = pascals[i-1]            
            currentrow.append(1)
            for j in range(1,i):
                currentrow.append(prevrow[j-1]+ prevrow[j])
            
            currentrow.append(1)            
            pascals.append(currentrow)        
        
        return pascals[-1]  