class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        ans = 0
        
        for w in words:
            if s.startswith(w):
                ans += 1
                
        return ans