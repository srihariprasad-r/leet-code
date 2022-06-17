class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        import sys
        d= {}
        mn = sys.maxsize
        for idx, el in enumerate(s):
            if el not in d:
                d[el] = [idx]
            else:
                d[el] =  d[el] + [idx]

        for _ , v in d.items():
            if len(v) == 1:
                mn = min(mn, v[0])
            
        if mn >= len(s):
            return -1
        else:
            return mn