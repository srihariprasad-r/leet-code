class Solution(object):
    def lengthOfLongestSubstring(self, s):
        substr = set()
        longest = 0
        left, right = 0, 0
        while right < len(s):
            if not (s[right] in substr):
                substr.add(s[right]) 
                right += 1
            else:
                substr.remove(s[left]) 
                left += 1                
                #right += 1
                
            if right - left > longest:
                longest = right - left
        
        return longest