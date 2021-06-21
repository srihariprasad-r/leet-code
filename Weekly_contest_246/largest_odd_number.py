class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        if len(num) == 0: return ""
        
        n = len(num)
        to_nums = 0
        
        check_odds = list(filter(lambda x: x if int(x) % 2 else 0, num))
        
        if len(check_odds) == 0:
            return ""

        to_nums = int(''.join(list(map(lambda x: x , num))))


        if to_nums % 2:
            return str(to_nums)
        else:
            while n > 0:
                to_nums = to_nums //10
                if to_nums % 2:
                    return str(to_nums)
                else:
                    n -= 1

        return ""