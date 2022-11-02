# wrong submission

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        def f(st):
            if len(st) == 0:
                return True
            
            for i in range(1, len(st)+1):
                if st[0:i+1] in wordDict and f(st[i+1:]):
                    return True

            return False
        
        return f(s)