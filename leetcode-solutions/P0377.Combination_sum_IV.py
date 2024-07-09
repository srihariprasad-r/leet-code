# TLE submission

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = []
        
        if target > sum(nums): return 0

        def dfs(cur, csum):
            if sum(cur) > target:
                return
            if sum(cur) == target:
                if cur not in res:
                    res.append(cur)
                return
            
            for n in nums:
                dfs(cur + [n], target - n)

            return len(res)
        
        return dfs([], target)

# Method 2


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def dfs(s, dp):
            if s == target:
                return 1

            if s > target:
                return 0

            if dp[s] > -1:
                return dp[s]

            ans = 0
            for num in nums:
                if s + num <= target:
                    ans += dfs(s + num, dp)
                    dp[s] = ans

            return ans

        dp = [-1] * (target+1)
        return dfs(0, dp)

# TLE
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def f(s):
            if s > target : return 0            
            if s == target: 
                return 1

            cnt = 0
            for n in nums:
                cnt += f(s + n)

            return cnt

        return f(0)        
