class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        dp = [0] * len(arr)
    
        for i in range(len(arr)):
            curmax = 0
            for j in range(1,k+1):
                if i-j+1 >= 0:
                    curmax = max(curmax, arr[i-j+1])
                    temp = dp[i-j] if i >=j else 0
                    dp[i] = max(dp[i], temp+(curmax*j))
    
        return dp[-1]

# Method 2 - almost same
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * len(arr)

        for i in range(len(arr)):
            mx = 0
            for j in range(1, k+1):
                if i - j + 1 >= 0:
                    mx = max(mx, arr[i-j+1])
                    dp[i] = max(dp[i], (dp[i-j] if i >= j else 0) + mx * j)

        return dp[-1]