class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip().split(' ')
        s = [c for c in s if len(c.strip()) > 0]
        i = 0
        j = len(s) - 1

        while i < j:
            tmp = s[j]
            s[j] = s[i]
            s[i] = tmp
            i += 1
            j -= 1

        return " ".join(s)
