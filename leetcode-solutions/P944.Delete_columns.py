class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def check(x, y):
            return x < y if x != y else True
        
        cnt = 0
        res = 0
        dct = {}
        for i in range(len(strs)):
            for j in range(len(strs[i])):
                dct.setdefault(j,[]).append(ord(strs[i][j]))
                
        for k, v in dct.items():
            cnt = 0 
            m = 1
            while m < len(v):
                if not(check(v[m-1], v[m])):
                    cnt += 1
                m += 1
            if cnt > 0:
                res  += 1
        
        return res