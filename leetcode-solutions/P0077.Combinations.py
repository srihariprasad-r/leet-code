class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []

        def dfs(idx, arr=[]):
            if len(arr) == k:
                res.append(copy.deepcopy(arr))
                return

            for i in range(idx, n+1):
                dfs(i+1, arr + [i])

            return res

        return dfs(1)
