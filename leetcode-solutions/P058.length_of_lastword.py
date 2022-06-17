class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        output = cnt = 0 
        for i in range(len(s)):
            if s[i] == ' ':
                cnt = 0
            else:
                cnt += 1
                output = cnt
        
        return output