class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dct = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in dct:
                dct[str(s[i])] = 1
            else:
                dct[str(s[i])] += 1

        tlen = len(t)
        j = 0

        while tlen > 0:
            if t[j] in dct:
                dct[str(t[j])] -= 1

                if dct[str(t[j])] == 0:
                    del dct[str(t[j])]

            tlen -= 1
            j += 1

        return True if len(dct) == 0 else False
