class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        import heapq
        lst = []
        for i in range(len(arr)):
            heapq.heappush(lst, (-(abs(arr[i]-x)),-arr[i]))
        
        while len(lst) > k:
            heapq.heappop(lst)
                
        return sorted([-el for _, el in lst])

# Method 2


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(arr)
        left = 0
        right = n - k

        while left < right:
            mid = left + (right-left)//2
            if x - arr[mid] > arr[mid+k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[right: right+k]
