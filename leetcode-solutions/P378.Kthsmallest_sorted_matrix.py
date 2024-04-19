class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        newlist = [j for i in matrix for j in i]
        
        newlist.sort()
        return newlist[k-1]

# Method 2

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        
        pq = []
        
        for i in range(n):
            heapq.heappush(pq, (matrix[0][i], 0, i))
        
        while k > 1:
            nums, row, col = heapq.heappop(pq)

            if row < n - 1:
                heapq.heappush(pq, (matrix[row+1][col], row+1, col))
                
            k -= 1
            
        return pq[0][0]

# Method 3
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        heapq.heapify(arr)

        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                heapq.heappush(arr, -matrix[m][n])
                
        while len(arr) > k:
            heapq.heappop(arr)
        
        return -heapq.heappop(arr)