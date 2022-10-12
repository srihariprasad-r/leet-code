# Wrong submission

class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        target = sum([abs(num) for num in nums])

        def recursion(idx, target, dp, msum):
            if idx < 0 or target < 0 or target > msum:
                return

            if idx == 0:
                if nums[idx] == target:
                    return True
                else:
                    return False

            if target == 0:
                return True

            if dp[idx][target] != -1:
                return dp[idx][target]

            not_take = recursion(idx-1, target, dp, msum)
            take = recursion(idx-1, target - nums[idx], dp, msum)

            dp[idx][target] = take or not_take

            return dp[idx][target]

        dp = [[-1 for _ in range(target+1)] for _ in range(n+1)]

        for j in range(n):
            dp[j][0] = True

        dp[0][0] = True

        for i in range(1, target+1):
            recursion(n-1, i, dp, target)

        min_diff = float('inf')

        for i in range(0, target/2 + 1):
            if dp[n-1][i]:
                min_diff = min(min_diff, abs(target - i) - i)

        return min_diff
