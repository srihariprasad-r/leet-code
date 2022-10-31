# wrong submission

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        cnt = defaultdict(int)
        
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if s[i:i+len(w)] == w:
                    cnt[w] += 1
                    break

        for w in wordDict:
            if w not in cnt.keys():
                return False
            
        return True