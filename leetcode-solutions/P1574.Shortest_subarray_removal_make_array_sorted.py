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
            
        if peak == len(arr) - 1:
            return 0
            
        while valley > peak and arr[valley-1] <= arr[valley]:
            valley -= 1
        
        ans = min(len(arr)-peak-1, valley)

        i = 0
        j = valley
        
        while i <= peak and j < len(arr):
            if arr[j] >= arr[i]:
                ans = min(ans, j - i - 1)
                i += 1
            else:
                j += 1
            
        return ans

# same as above

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        i = 0
        j = len(arr) - 1
        ans = 0

        while i < len(arr)-1 and arr[i] <= arr[i+1]:
            i += 1

        # need this condition
        if i == len(arr) - 1: return 0

        while j > i and arr[j-1] <= arr[j]:
            j -= 1

        ans = min(len(arr)- i-1, j)

        m = 0
        n = j
        while m <= i and n < len(arr):
            if arr[n] >= arr[m]:
                ans = min(ans, n - m -1)
                m += 1
            else:
                n += 1

        return ans