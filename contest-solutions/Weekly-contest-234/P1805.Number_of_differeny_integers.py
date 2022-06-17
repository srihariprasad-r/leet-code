class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        number = set()
        tmp = ""
        for i in word:
            if i.isdigit():
                tmp += i
            else:
                if len(tmp) > 0:
                    if len(tmp.lstrip('0')) == 0:
                        number.add(int(tmp))
                    elif len(tmp.lstrip('0')) > 0:
                        number.add(int(tmp.lstrip('0')))
                tmp = ""
                
        if len(tmp) > 0:
            if len(tmp.lstrip('0')) > 0:
                number.add(int(tmp.lstrip('0')))
            elif len(tmp.lstrip('0')) == 0:
                number.add(int(tmp))
        
        return len(number)