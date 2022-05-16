class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []

        tsum = sum(i for i in range(n+1))

        if k > n or n > tsum:
            return []

        def dfs(idx, lst, csum):
            if len(lst) > k or csum > n:
                return []

            if len(lst) == k and csum == n:
                ans.append(copy.deepcopy(lst))

            for i in range(idx+1, 10):
                dfs(i, lst+[i], csum+i)

            return ans

        return dfs(0, [], 0)
