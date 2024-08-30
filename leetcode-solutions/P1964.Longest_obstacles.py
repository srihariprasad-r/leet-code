class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        dp = [float('inf')] * len(obstacles)
        res = [1] * len(obstacles)

        dp[0] = obstacles[0]

        def bs(arr, tgt):
            l = 0
            r = len(arr)-1

            while l < r:
                mid = l + (r-l) // 2
                if arr[mid] <= tgt:
                    l = mid + 1
                else:
                    r = mid-1

            return l

        for i in range(1, len(obstacles)):
            if obstacles[i] >= dp[i-1]:
                dp[i] = obstacles[i]
                res[i] = i+1
            else:
                idx = bs(dp, obstacles[i])
                dp[idx] = obstacles[i]
                res[i] = max(res[i], idx+1)

        return res