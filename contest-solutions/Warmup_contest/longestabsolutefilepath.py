class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        prelen, maxlen = 0, 0
        inpdir = input.split("\n")
        dirlen = [0] * (len(inpdir)+1)
        for i in range(len(inpdir)):
            lvl = inpdir[i].count('\t')
            curlen = len(inpdir[i]) - lvl 
            if lvl == 0:
                prelen = 0
            else:
                prelen = dirlen[lvl -1]
        
            if inpdir[i].count('.') >= 1:
                maxlen = max(prelen + curlen, maxlen)
            else:
                dirlen[lvl] = prelen + curlen + 1
    
        return maxlen