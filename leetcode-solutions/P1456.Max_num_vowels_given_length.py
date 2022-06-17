class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cnt = 0
        res = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        j = 0
        i = 0
        for ch in s:
            if ch in vowels:
                cnt += 1
            while i - j +1 > k:
                if s[j] in vowels: cnt -= 1
                j += 1
            res = max(res, cnt)
            i += 1
        
        return res