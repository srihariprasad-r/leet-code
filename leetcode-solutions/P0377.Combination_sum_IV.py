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

# Method 2 - TLE

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def dfs(s):
            if s == target:
                return 1

            if s > target:
                return 0

            ans = 0
            for num in nums:
                if s + num <= target:
                    ans += dfs(s + num)

            return ans

        return dfs(0)
