class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        ans = list()

        def dfs(cur, idx, res):
            if idx == n:
                if res not in ans:
                    ans.append(res)
                return

            dfs(cur, idx+1, res)
            dfs(cur, idx + 1, res + [cur[idx]])

            return ans

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            return dfs(nums[i:], i, [])