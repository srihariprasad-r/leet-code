class Solution:
    def maxCoins(self, arr: List[int]) -> int:
        dp = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
        for i in range(len(arr)):
            dp[i][i] = ((arr[i]) \
            * (arr[i-1] if i -1 > -1 else 1) * (arr[i+1] if i + 1 < len(arr) else 1))
            
        l = 2
        while l <= len(arr):
            i = 0
            while i <= len(arr) - l:
                j = i + l - 1
                k = i
                while k <= j:
                    s = ((arr[i-1] if i-1>-1 else 1) \
                    * (arr[k])* (arr[j+1] if j + 1 < len(arr) else 1))
                    s += dp[i][k-1] if k - 1 >= i else 0
                    s += dp[k+1][j] if k + 1 <= j else 0
                    dp[i][j] = max(dp[i][j], s)
                    k += 1
                i += 1
            l += 1
            
        return dp[0][len(arr)-1]

# wrong submission
class Solution:
    def maxCoins(self, arr: List[int]) -> int:
        dp = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
        mx = float('-inf')

        for g in range(len(dp)):
            i = 0            
            for j in range(g,len(dp)):              
                for k in range(i, j+1):
                    left = dp[i][k-1] if k != i else 0
                    right = dp[k+1][j] if k != j else 0
                    val = left + right + ((arr[i-1] if i > 0 else 1)* (arr[k])*(arr[j+1] if j < len(arr)-1 else 1))

                    if val > mx: mx = val

                dp[i][j] = mx
                i += 1


        return dp[0][len(arr)-1]