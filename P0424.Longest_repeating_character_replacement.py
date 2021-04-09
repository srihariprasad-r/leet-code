class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cnt = {}
        res = 0
        max_val = 0
        j = 0
        i = 0
        for ch in s:
            if not(ch in cnt):
                cnt[ch] = 1
            else:
                cnt[ch] += 1
            max_val = max(max_val, cnt[s[j]])
            if j - i +1 - max_val > k:
                cnt[s[i]] -= 1
                if cnt[s[i]] == 0:
                    del cnt[s[i]]
                i += 1
            res = max(res, j-i+1)
            j += 1
        
        return res