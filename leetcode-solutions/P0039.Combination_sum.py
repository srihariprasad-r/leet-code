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
