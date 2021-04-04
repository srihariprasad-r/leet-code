class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        ans = [0]* k
        dct = {}
        res = {}
        for i in range(len(logs)):
            lid, ltime = logs[i]
            dct.setdefault(lid, set()).add(ltime)

        for m, n in dct.items():
            if not(len(n) in res):
                res[len(n)] = 1
            else:
                res[len(n)] += 1
        
        for i in range(1, k+1):
            if i in res:
                ans[i-1] = res[i]
        
        return ans