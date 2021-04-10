class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = -1
        b = 1
        cnt = 0
        res = 0
        splitcnt = 0
        for ch in s:
            if ch == 'L':
                cnt -= 1
            else:
                cnt += 1

            if cnt == 0:
                res += 1
                splitcnt = max(splitcnt, res)
        
        return splitcnt