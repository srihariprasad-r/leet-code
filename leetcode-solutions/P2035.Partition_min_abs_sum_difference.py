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


# wrong submission
class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = float('inf')
        total = sum(nums)
        half = total//2

        def dfs(idx, csum, lst, arr):
            if idx == len(lst):
                arr.append(csum)
                return

            dfs(idx+1, csum, lst, arr)
            dfs(idx+1, csum+lst[idx], lst, arr)

            return

        sum1 = []
        sum2 = []
        n = len(nums)
        N = n//2
        dfs(0, 0, nums[0:n//2], sum1)
        dfs(0, 0, nums[n//2:], sum2)

        ans = abs(sum(sum1) - sum(sum2))

        for m in range(1, n):
            left = sum1[:m+1]
            right = sum2[N-m:]
            right.sort()

            for s in left:
                remain = half - s
                p = bisect.bisect_left(right, remain)
                for i in [p, p-1]:
                    if 0 <= i < len(right):
                        l = s + right[i]
                        r = total - l
                        diff = abs(l - r)
                        ans = min(ans, diff)

        return ans