class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        stck = []
        
        for i in range(len(arr)):
            j = i + 1
            if j < len(arr): 
                max_el = max(arr[j:])
                stck.append(max_el)    
        
        stck.append(-1)
        
        return stck