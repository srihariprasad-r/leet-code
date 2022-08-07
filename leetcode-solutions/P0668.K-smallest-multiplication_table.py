class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        def check(x, m, n):
            cnt = 0
            for v in range(1, m+1):
                el = min(x//v, n)
                cnt += el

            return cnt >= k

        left = 1
        right = m * n

        while left < right:
            mid = left + (right-left)//2

            if check(mid, m, n):
                right = mid
            else:
                left = mid + 1

        return left
