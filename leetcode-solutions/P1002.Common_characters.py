class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        chr_array = [float('inf')] * 26
        res = []
        
        for s in words:
            s_array = [0] * 26
            for c in s:
                s_array[ord(c)-ord('a')] += 1
                
            for idx, v in enumerate(s_array):
                chr_array[idx] = min(s_array[idx], chr_array[idx])
                
        for idx, c in enumerate(chr_array):
            while c > 0:
                res.append(chr(idx + ord('a')))
                c -= 1
            
        return res