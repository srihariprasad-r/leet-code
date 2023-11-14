class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1: 
            return 1

        if len(arr) == 2:
            if arr[0] != arr[1]: 
                return 2
            else:
                return 1

        dp = [0] * len(arr)
        res = 0

        dp[0] = 1
        dp[1] = 1

        if arr[0] != arr[1]:
            dp[1] = 2

        for i in range(2,len(arr)):
            if arr[i] == arr[i-1]:
                dp[i] = 1
            else:
                if arr[i-1] == arr[i-2]: 
                    dp[i] = 2
                else:
                    # [_, 4, 2, 10] i == 3
                    # (10-2)*(2-4) = 2 * -2 = -4
                    if (arr[i] - arr[i-1]) * (arr[i-1]- arr[i-2]) < 0:
                        dp[i] = dp[i-1] + 1
                    else:
                        dp[i] = 2

            res = max(res, dp[i])

        return res

            


