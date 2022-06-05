class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        peak = ans = 0
        valley = len(arr) - 1
        
        while peak < len(arr) - 1 and arr[peak+1] >= arr[peak]:
            peak += 1
            
        while valley > peak and arr[valley-1] <= arr[valley]:
            valley -= 1
        
        ans = min(len(arr)-peak-1, valley)

        i = peak
        j = valley
        
        while j < len(arr):
            if arr[j] >= arr[i]:
                ans = min(ans, j - i - 1)
            j += 1
            
        return ans
            