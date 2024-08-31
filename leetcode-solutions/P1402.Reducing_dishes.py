class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        def recursion(idx, t):
            if idx >= len(satisfaction): return 0

            take = (t * satisfaction[idx]) + recursion(idx+1, t + 1)
            no_take = recursion(idx+1, t)

            return max(take, no_take)

        return recursion(0,1)