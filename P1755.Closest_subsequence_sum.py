class Solution(object):
    def minAbsDifference(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        ans = float('inf')

        def dfs(idx, csum, lst, res):
            if idx == len(lst):
                res.append(csum)
                return

            dfs(idx+1, csum, lst, res)
            dfs(idx+1, csum+lst[idx], lst, res)

            return

        sum1 = []
        sum2 = []
        n = len(nums)
        dfs(0, 0, nums[0:n//2], sum1)
        dfs(0, 0, nums[n//2:], sum2)

        sum2.sort()

        for s in sum1:
            tgt = goal - s
            idx = bisect_left(sum2, tgt)

            if idx > 0:
                ans = min(ans, abs(tgt-sum2[idx-1]))

        return ans
