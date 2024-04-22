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

# Method 2
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1

        while l < r:
            mid = l + (r-l+1)//2

            if 0 < mid < len(arr) - 1:
                if arr[mid - 1] < arr[mid] > arr[mid+1]:
                    return mid
                else:
                    if arr[mid] < arr[mid+1]:
                        l += 1
                    else:
                        r -= 1
            
        return r