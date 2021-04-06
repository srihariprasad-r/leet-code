class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        stck = []
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        S = list(s)
        i = 0 
        j = len(s) - 1
        while i < j:
            if S[i] in vowels and S[j] in vowels:
                S[i], S[j] = S[j], S[i]
                i += 1
                j -= 1
            elif not(S[i] in vowels):
                i += 1
            elif not(S[j] in vowels):
                j -= 1
            
        return ''.join(S)