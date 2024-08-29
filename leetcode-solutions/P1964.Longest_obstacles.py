class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        dp = [1] * len(obstacles)

        for i in range(1, len(obstacles)):
            for j in range(0,i):
                if obstacles[i] >= obstacles[j]:
                    dp[i] = 1 + dp[j]

        return dp