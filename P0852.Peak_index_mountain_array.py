class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        r = len(arr) - 1 
        l = 0
        while l < r:
            mid = (l+r)/2
            if arr[mid] < arr[mid+1]:
                l += 1
            else:
                r = mid
        
        return l