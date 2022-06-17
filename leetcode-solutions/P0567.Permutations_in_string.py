class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        cnt_s1 = {}
        for ch in s1:
            if not(ch in cnt_s1):
                cnt_s1[ch] = 1
            else:
                cnt_s1[ch] += 1
                
        j = 0 
        i = 0
        for ch in s2:
            if ch in cnt_s1:
                cnt_s1[ch] -= 1
            while j - i + 1 > len(s1):
                if s2[i] in cnt_s1:
                    cnt_s1[s2[i]] += 1
                i += 1
            j += 1

            if max(v for v in cnt_s1.values()) == 0:
                return True
       
        return False