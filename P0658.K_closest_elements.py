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