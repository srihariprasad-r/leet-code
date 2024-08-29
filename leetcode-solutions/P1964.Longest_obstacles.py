class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        dp = [1] * len(obstacles)

        for i in range(1, len(obstacles)):
            cnt = 0
            for j in range(0,i):
                if obstacles[i] >= obstacles[j]:
                    dp[i] = max(dp[i], dp[j]+1) 

        return dp