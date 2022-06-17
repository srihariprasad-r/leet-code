class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        dict = [0]* 26
        for ch in S:
            ascii = ord(ch)-ord('a')
            dict[ascii] += 1 
            

        maxfreq = 0
        maxidx = 0
        for i in range(len(dict)):
            if dict[i]> maxfreq: 
                maxfreq = dict[i]
                maxidx = i

        if maxfreq > (len(S)+1)//2 : return ''  
        
        res = ['']*len(S)
        idx = 0
        while dict[maxidx]:
            res[idx] = chr(maxidx+ord('a'))
            idx += 2
            dict[maxidx] -= 1

        for j in range(26):
            while dict[j] > 0:
                if idx >= len(res):
                    idx = 1
                res[idx] = chr(j+ord('a'))
                idx += 2
                dict[j] -= 1

        return ''.join(res) if len(res) > 0 else ''