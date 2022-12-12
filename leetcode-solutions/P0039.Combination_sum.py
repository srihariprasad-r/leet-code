class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def dfs(cur, csum, idx):
            if csum > target:
                return
            if csum == target:
                if cur not in res:
                    res.append(copy.deepcopy(cur))
                return

            for i in range(idx, len(candidates)):
                dfs(cur+[candidates[i]], csum + candidates[i], i)

            return res

        return dfs([], 0, 0)

# Method 2 

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(idx, s, arr, res):
            if s == target:
                res.append(copy.deepcopy(arr))
                return

            if idx >= len(candidates) or s > target:
                return

            take = dfs(idx, s + candidates[idx], arr + [candidates[idx]], res)
            no_take = dfs(idx + 1, s, arr, res)

            return res

        return dfs(0, 0, [], [])