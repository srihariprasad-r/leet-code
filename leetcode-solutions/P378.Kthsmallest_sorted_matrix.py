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
    
# Method 4
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = matrix[0][0]
        r = matrix[-1][-1]
        ans = 0

        def f(a):
            c = len(matrix[0]) - 1

            res = 0
            for r in range(len(matrix)):
                while c >= 0 and matrix[r][c] > a:
                    c -= 1

                res += c + 1

            return res

        while l <= r:
            mid = (r+l)//2

            if f(mid) >= k:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans