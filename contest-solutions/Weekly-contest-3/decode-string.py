class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = []
        nums = 0
        str = ''
        for k in s:
            if k.isdigit():
                nums = nums*10 + int(k)
            elif k.isalpha():
                str += k
            elif k == '[':
                arr.append(nums)
                arr.append(str)
                nums = 0
                str = ''
            else:
                pstr = arr.pop()
                pnum = arr.pop()
                str = pstr + pnum * str

        return str