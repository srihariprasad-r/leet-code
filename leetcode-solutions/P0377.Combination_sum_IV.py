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