class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        def isSubSeq(words):
            idx = -1
            
            for c in words:
                if c not in map:
                    return False
                
                el = bisect_right(map[c], idx)
                
                if el == len(map[c]):
                    return False
                
                idx = map[c][el]
            
            return True
        
        ans = 0
        map = defaultdict(list)

        for idx, c in enumerate(s):
            map[c].append(idx)
            
        for word in words:
            if isSubSeq(word):
                ans += 1
                
        return ans