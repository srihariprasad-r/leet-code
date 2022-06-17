class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        diffarr = []
        minval = 99999999
        arr.sort()
        for i in range(len(arr) - 1):
            diff = abs(arr[i] - arr[i+1])
            if diff < minval:
                minval = diff
                diffarr = []
                diffarr.append([arr[i], arr[i+1]])
            elif diff == minval:
                diffarr.append([arr[i], arr[i+1]])
                
        return diffarr