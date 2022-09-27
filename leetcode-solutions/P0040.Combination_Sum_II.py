class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        candidates.sort()

        def dfs(cur, csum, idx):
            if csum > target:
                return
            if csum == target:
                if cur not in res:
                    res.append(cur)
                return

            for i in range(idx, len(candidates)):
                # dfs(cur, csum, i + 1)
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                dfs(cur + [candidates[i]], csum + candidates[i], i + 1)

            return res

        return dfs([], 0, 0)
