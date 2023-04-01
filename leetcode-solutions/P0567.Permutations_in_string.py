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
    
# Method 2
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = Counter(s1)
        w = defaultdict(int)
        valid = 0

        left = 0
        right = 0

        while right < len(s2):
            c = s2[right]
            if c in cnt:
                w[c] += 1
                if w[c] == cnt[c]:
                    valid += 1

            right += 1

            while right - left >= len(s1):
                if valid == len(cnt):
                    return True
                d = s2[left]
                left += 1
                if d in cnt:
                    if w[d] == cnt[d]:
                        valid -= 1
                    w[d] -= 1

        return False