# Wrong submission

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        ans = list()

        def dfs(cur, idx):
            if idx == n:
                ans.append(cur)
                return

            dfs(cur, idx+1)
            dfs(cur + [nums[idx]], idx + 1)

            return ans

        return dfs([], 0)
