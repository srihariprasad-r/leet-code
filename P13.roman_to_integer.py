class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I' : 1 , 
                 'V': 5, 
                 'X':10,
                 'L':50, 
                 'C':100, 
                 'D':500 , 
                 'M':1000 }
        rem = 0
        for i in range(0,len(s)):
            if i > 0 and roman.get(s[i]) > roman.get(s[i-1]):
                rem += roman.get(s[i]) - 2 * (roman.get(s[i-1]))
            else:
                rem += roman.get(s[i])
        
        return rem