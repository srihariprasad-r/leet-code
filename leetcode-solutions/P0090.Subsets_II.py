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
        
# Method 2
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        ans = []
        nums.sort()

        def recursion(idx, arr):
            if not(res in ans):
                ans.append(copy.deepcopy(res))

            for i in range(idx, len(arr)):
                res.append(arr[i])
                recursion(i+1, arr)
                res.pop()

            return ans

        return recursion(0, nums)
