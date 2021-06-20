# need rework, test cases failing

class Solution(object):
    def largestMagicSquare(self, arr):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(arr) == 1: return 1
        m = len(arr[0])
        n = 0
        mx_k = -float('inf')

        while n < len(arr):
            rsum , csum, rdsum, ldsum = 0, 0, 0, 0
            for i in range(n, len(arr)-n+1):
                rsum += arr[n][i]

            for j in range(n, m-1):
                csum += arr[j][n]

            for k in range(n,m-1):
                rdsum += arr[k][k-n+1]

            for g in range(len(arr)-n):
                ldsum += arr[g+n][g+1]        

            if rsum == csum == rdsum == ldsum:
                mx_k = max(mx_k, len(arr)-n)

            n += 1

        return mx_k